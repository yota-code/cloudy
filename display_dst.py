#!/usr/bin/env python3

import math
import random

from cc_pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

cmap = matplotlib.colormaps['viridis']

dst_arr = Path("dst_arr_uint8_2deg.npy.br").load()

h, w = dst_arr.shape

m_lst = list(range(h))
random.shuffle(m_lst)

while m_lst :
	m = m_lst.pop(0)
	n_lst = list()
	for n in range(h) :
		if dst_arr[m,n] != 0 :
			n_lst.append(n)
		if dst_arr[n,m] != 0 :
			n_lst.append(n)

	n_arr = np.array(n_lst)

	d_lst = [dst_arr[max(m, n),min(m, n)] for n in n_lst]
	
	print(len(d_lst))

	xyz_arr = Path("xyz_arr.npy.br").load()
	x, y, z = xyz_arr[:,0], xyz_arr[:,1], xyz_arr[:,2]
	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')
	ax.set_box_aspect([1.0, 1.0, 1.0])
	ax.plot(x, y, z, alpha=0.3)
	ax.scatter(x[n_lst], y[n_lst], z[n_lst], c=[cmap(dst_arr[max(m, n),min(m, n)] / 255) for n in n_lst])
	ax.scatter(x[m], y[m], z[m], color="tab:red")
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	plt.show()
