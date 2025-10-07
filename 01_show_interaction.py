
#!/usr/bin/env python
# -*- coding:utf8 -*-
from pymol import cmd
from pymol.cmd import util
import sys
import os


def HBondA(pdb,lig):
    name = f'HBA_{lig}'
    #selection_1 = f'{lig} and (elem o or (elem n and not (neighbor hydro)))'
    selection_1 = f'{lig} and donors'
    selection_1_h = f'{lig} and elem h and (neighbor donors)'
    selection_2 = f'{pdb} and  acceptors'
    #当供体上的氢与受体之间的距离小于3A，判断为形成氢键，没有考虑角度
    dist = cmd.distance(name, selection_1_h, selection_2, '3', '0')
    return name

def HBondD(pdb,lig):
    name = f'HBD_{lig}'
    #selection_1 = f'{lig} and (elem n,o and (neighbor hydro))'
    #selection_2 = f'{pdb} and (elem o and (elem n and not (neighbor hydro)))'
    selection_1 = f'{pdb} and  donors'
    selection_1_h = f'{pdb} and  elem h and (neighbor donors)'
    selection_2 = f'{lig} and acceptors'
    dist = cmd.distance(name,selection_1_h,selection_2,'3', '0')
    return name


def Pi_Pi_interaction(pdb,lig):
    name = f'PI_PI_{lig}'
    selection_1 = lig
    selection_2 = pdb
    cmd.distance(name,selection_1,selection_2,'5.5','6')
    return name

def Cation_Pi_interaction(pdb,lig):
    name = f'PI_Cation_{lig}'
    selection_1 = lig
    selection_2 = pdb
    cmd.distance(name,selection_1,selection_2,'5.5','7')
    return name


def Salt_bridge_positive(pdb,lig):
    name = f'SBP_{lig}'
    selection_1 = f'{lig} and formal_charge >0 and elem N'
    selection_2 = f'{pdb} and resn ASP+GLU and name OD*+OE*'
    cmd.distance(name,selection_1,selection_2,'5.0','0')
    return name

def Salt_bridge_negative(pdb,lig):
    name = f'SBN_{lig}'
    selection_1 = f'{lig} and formal_charge < 0 and elem O'
    selection_2 = f'{pdb} and (resn LYS and name NZ) or (resn ARG and name NE+NH*)'
    cmd.distance(name,selection_1,selection_2,'5.0','0')
    return name

def run(complex,ions):

    #load pdb
    cmd.load(complex)
    #get pdb and lig name
    pdb_name = complex[:-4]
    lig_name = pdb_name + '_lig'
     #extract protein and ligand
    cmd.extract(f'delete_{pdb_name}', f'{pdb_name} and not polymer.protein ')
    cmd.extract(f'ions_{pdb_name}', f'delete_{pdb_name} and resn {ions}')
    cmd.extract(lig_name, f'delete_{pdb_name} and org.')
    cmd.h_add('all')
    cmd.show('spheres',f'ions_{pdb_name}')
    cmd.set('sphere_scale',0.3,f'ions_{pdb_name}')
    cmd.delete(f'delete_{pdb_name}')
    #label neighbor residues in receptor around ligand
    neighbor_res = f'{pdb_name} and (byres ({lig_name} around 4))'
    neighbor_res_ca = f'{neighbor_res} and name CA'
    cmd.select(f'res_ca_{pdb_name}', neighbor_res_ca)
    cmd.label(f'res_ca_{pdb_name}', 'oneletter+resi')
    cmd.set('label_bg_color', -7, '', 0)
    cmd.set('label_size', 14, '', 0)
    cmd.set('label_font_id', '18')
    cmd.select('neighbor_res', neighbor_res)
    cmd.show('sticks', neighbor_res)
    cmd.set('stick_radius', '0.1', pdb_name)
    cmd.select('donors_h', f'{pdb_name} and e. h and (neighbor donor)')
    util.cba(33, pdb_name)
    util.cba(156, lig_name)
    #print  Hbonds, salt-bridge, cation-pi and pi-pi stacking interactions
    HBA = HBondA(pdb_name, lig_name)

    HBD = HBondD(pdb_name, lig_name)

    PI = Pi_Pi_interaction(pdb_name, lig_name)

    C_PI = Cation_Pi_interaction(pdb_name, lig_name)

    SBP = Salt_bridge_positive(pdb_name, lig_name)

    SBN = Salt_bridge_negative(pdb_name, lig_name)

    cmd.set('dash_color', 'yellow', HBA)
    cmd.set('dash_color', 'yellow', HBD)
    cmd.set('dash_color', 'teal', PI)
    cmd.set('dash_color', 'teal', C_PI)
    cmd.set('dash_color', 'pink', SBP)
    cmd.set('dash_color', 'pink', SBN)
    cmd.do(f'group {pdb_name}_,{pdb_name} {lig_name} ions_{pdb_name} res_ca_{pdb_name} {HBA} {HBD} {PI} {C_PI} {SBP} {SBN}')
    cmd.hide('stick', f'{lig_name} and e. h  and (neighbor e. c)')
    cmd.hide('stick', f'{pdb_name} and e. h  and (neighbor e. c)')
    cmd.set('dash_radius', '0.07')
    cmd.set('dash_gap', '0.3')

def main():
    work_path = sys.argv[1]

    cmd.delete('all')
    cmd.set('bg_rgb','white')
    cmd.set('cartoon_color', 'gray90')
    cmd.set('cartoon_transparency', 0.6)
    # get file_name and load them (a receptor and ligands)
    os.chdir(work_path)
    files = os.listdir()
    #complex_proteins = [x for x in files if x.endswith('.pdb')]
    complex_names = [x for x in files if x.endswith('.pdb')]
    if len(complex_names)>30:
        complex_names = [x for x in files if x.endswith('.pdb')][:30]
    #ions = 'Ca,Mg,Zn,Mn,Cu,Fe,Co,Pt,Ni,Mo,Rh,Ti,Ag,Pd,Cr,V,As,Sc,Ba,Al,Ga,In,Ti'
    ions='Cl,NA'
    ions ='+'.join(ions.split(','))
    for com in complex_names:
        run(com, ions)
    cmd.save('protein_ligand_interactions.pse')

main()