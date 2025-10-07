#!/home/rdkibler/.conda/envs/pyro/bin/python3

import argparse
import pymol
import numpy as np
from sklearn import metrics
from matplotlib import pyplot as plt
import os

parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["r_hydration","r_","histogram","contact_map"])
parser.add_argument("pdb")

args = parser.parse_args()

pymol.cmd.load(args.pdb,"pose")



if args.mode == "r_hydration":
	coords = np.array([a.coord for a in pymol.cmd.get_model("pose").atom])
	distances = metrics.pairwise.euclidean_distances(coords).flatten()
	print(np.max(distances)/2.0)
if args.mode == "histogram":
	coords = np.array([a.coord for a in pymol.cmd.get_model("pose").atom])
	distances = metrics.pairwise.euclidean_distances(coords).flatten()
	plt.hist(distances,bins=np.arange(min(distances), max(distances) + 1, 1))
	bn = os.path.splitext(os.path.basename(args.pdb))[0]
	plt.title(f"distance histogram for {bn}")
	plt.xlabel("distance")
	plt.ylabel("fequency")

	plt.savefig(f"{bn}_distance_histogram.png")
	print(f'Saved histogram to {bn}_distance_histogram.png')

if args.mode == "r_gyration":
	print("not implemented :(")

if args.mode == "contact_map":
	#print(dir(pymol.cmd.get_model("pose").atom[0]))
	#print(pymol.cmd.get_model("pose").atom[1].name)


	coords = np.array([a.coord for a in pymol.cmd.get_model("pose").atom if a.name == "CA"])
	bn = os.path.splitext(os.path.basename(args.pdb))[0]
	distances = metrics.pairwise.euclidean_distances(coords)
	cmap = plt.get_cmap("inferno_r")
	plt.imshow(distances,cmap=cmap)
	plt.title("Residue-residue Ca distance map")
	plt.xlabel("Residue i")
	plt.ylabel("Residue j")
	plt.savefig(f"{bn}_distance_map.png")
	print(f'Saved distance map to {bn}_distance_map.png')

	#print(distances)