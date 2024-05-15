#!/usr/bin/env python3

import math

from cc_pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

txt = Path("uniform_snap_10hz.tsv").read_text()
aze_arr = np.array([
    [float(i) for i in line.split('\t')]
    for line in txt.splitlines()
])

azimuth = aze_arr[:,0]
elevation = aze_arr[:,1]

h, w = aze_arr.shape

xyz_arr = np.zeros((h, 3))
xyz_arr[:,0] = np.cos(elevation) * np.cos(azimuth)
xyz_arr[:,1] = np.cos(elevation) * np.sin(azimuth)
xyz_arr[:,2] = np.sin(elevation)
x, y, z = xyz_arr[:,0], xyz_arr[:,1], xyz_arr[:,2]

Path("xyz_arr.npy.br").save(xyz_arr)

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
        if m != n :
            u = np.sum(xyz_arr[m,:] * xyz_arr[n,:])
            if u > r :
                dist_arr[m,n] = int(math.acos(u) * 32)
                i += 1
    print(m, h, i, 100.0 * m / h)

print("save")
Path("dist_arr.npy.br").save(dist_arr)