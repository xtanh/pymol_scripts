# Derrick
# Edit by Hua
# This script should create pymol objects containing all residues belonging to a PDBinfo label

import re, string, gzip
import random as random
from pymol import cmd, cgo, util
from collections import defaultdict
import os
from matplotlib import cm
from itertools import cycle

def set_random_rgb_color(obj_name):
    levels = list(range(1,256,32))
    tmp_color=tuple(random.choice(levels) for _ in range(3))
    print(tmp_color)
    cmd.set_color("tmp_color_%s"%obj_name, "[%s,%s,%s]"%(tmp_color[0],tmp_color[1],tmp_color[2]))
    cmd.color("tmp_color_%s"%obj_name, "%s"%obj_name)

def create_PDBinfo_objs( lines, name ):
    model = cmd.get_model(name)
    PDBinfo_objects = []

    PDBinfo_dict = defaultdict(list)
    for line in lines:
        info_list = line.split()
        assert info_list[0] == "REMARK"
        assert info_list[1] == "PDBinfo-LABEL:"
        res_idx = info_list[2]
        res_labels = info_list[3:]
        for each_label in res_labels:
            if each_label == "B" or each_label == "A": continue
            PDBinfo_dict[each_label].append(res_idx)

    for key in PDBinfo_dict:
        print(key, "residues = ", PDBinfo_dict[key])

    color_list = (cm.get_cmap("Accent").colors)
    color_iter = cycle(color_list)

    for ii, key in enumerate(PDBinfo_dict):
        res_string = "+".join(PDBinfo_dict[key])
        cmd.select(key, f"resi {res_string}")
        this_color = [int(x*256) for x in next(color_iter)]
        new_color_name = f"new_color_{ii}"
        cmd.set_color(new_color_name, this_color)
        cmd.color(new_color_name, key)
        util.cnc(key)
        cmd.disable(key)

def get_PDBinfo():
    # look in object list for rosetta pdb's with source files in pwd
    # print(cmd.get_names())
    for name in cmd.get_names()[:1]:
        lines = []
        if os.path.exists(f"{name}.pdb"):
            with open(f"{name}.pdb", "r") as f:
                lines = [ x for x in f.readlines() ]
        elif os.path.exists(f"{name}.pdb.gz"):
            with gzip.open(f"{name}.pdb.gz", "r") as f:
                lines = [ x.decode("utf-8") for x in f.readlines() ]
        else:
            print(f"Cannot find source pdb file for {name}")
            continue

        PDBinfo_lines = [ x for x in lines if x.startswith("REMARK PDBinfo-LABEL") ]

        if not PDBinfo_lines:
            print(f"no PDBinfo lines found for {name}")
        else:
            print(f"Showing Rosetta PDBinfo for {name}...")
            create_PDBinfo_objs( PDBinfo_lines, name )

def save_as_session(): #Save a pymol session with the name of the first object
        objs=cmd.get_object_list()
        tmp_model_name="./"+objs[0]+".pse"
        print("Saving Pymol Session file as:", tmp_model_name)
        cmd.save(tmp_model_name, format="pse")

cmd.extend('pdbinfo', get_PDBinfo)
cmd.extend('save_pse', save_as_session)
