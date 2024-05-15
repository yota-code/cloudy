#!/usr/bin/env python3

import math

from cc_pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

txt = Path("azimuth_elevation.tsv").read_text()
ae_arr = np.array([
	[float(i) for i in line.split('\t')]
	for line in txt.splitlines()
])

azimuth = ae_arr[:,0]
elevation = ae_arr[:,1]

Path("ae_arr.npy.br").save(ae_arr)

h, w = ae_arr.shape

xyz_pth = Path("xyz_arr.npy.br")

if not xyz_pth.is_file() :
	xyz_arr = np.zeros((h, 3))
	xyz_arr[:,0] = np.cos(elevation) * np.cos(azimuth)
	xyz_arr[:,1] = np.cos(elevation) * np.sin(azimuth)
	xyz_arr[:,2] = np.sin(elevation)
	xyz_pth.save(xyz_arr)
else :
	xyz_arr = xyz_pth.load()

x, y, z = xyz_arr[:,0], xyz_arr[:,1], xyz_arr[:,2]

if False :
	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')
	ax.scatter(x, y, z)

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.show()

dist_arr = np.zeros((h, h), dtype=np.uint8)

r = math.cos(math.radians(255/32))

for m in range(h) :
	i = 0
	for n in range(m) :
		u = np.sum(xyz_arr[m,:] * xyz_arr[n,:])
		if u > r :
			# print(u, math.acos(u), math.degrees(math.acos(u)) * 32)
			dist_arr[m,n] = int(math.degrees(math.acos(u)) * 32)
			i += 1
	print(m, h, i, 100.0 * m / h)

print("save")
Path("dst_arr.npy.br").save(dist_arr)
