#!/usr/bin/env python3

import ast
import collections
import sys

import numpy as np
import matplotlib.pyplot as plt

from cc_pathlib import Path

def load_pcd(pth) :
	h_lst = ['x', 'y', 'z', 'reflectance', 'azimuth', 'elevation', 'distance', 'line_no', 'eye_no']
	m_map = {
		0 : collections.defaultdict(list),
		1 : collections.defaultdict(list),
	}
	is_data = False
	for line in pth.read_text().splitlines() :
		if line == 'DATA ascii' :
			is_data = True
			continue
		if is_data :
			v_lst = [ast.literal_eval(v) for v in line.split()]
			x, y, z, reflectance, azimuth, elevation, distance, line_no, eye_no = v_lst
			assert len(v_lst) == len(h_lst)
			m_map[eye_no][line_no].append([azimuth, elevation, distance, reflectance])
			
	# Path("test.json").save(m_map, filter_opt={'verbose':True})			
	# Path("test.pickle.br").save(m_map)			
	
	for e in m_map :
		for n in m_map[e] :
			m_map[e][n] = np.array(m_map[e][n])
		print(min(m_map[e].keys()), max(m_map[e].keys()))

	return m_map
    
if __name__ == '__main__' :
	p_lst = ['+', 'x']
	
	c_lst = [
		plt.get_cmap('autumn'),
		plt.get_cmap('winter')
	]
	
	for i, arg in enumerate(sys.argv[1:]) :
		m_map = open_pcd(Path(arg))
		for e in [0,] :
			for n in range(24) :
				azimuth = m_map[e][n][:,0]
				elevation = m_map[e][n][:,1]
				u = np.cos(elevation) * np.sin(azimuth)
				v = np.sin(elevation)
				# plt.plot(u, v, marker=p_lst[i % len(p_lst)], linewidth=(5 if i == 0 else 2), color=c_lst[i%len(c_lst)](n / 31))
				plt.plot(azimuth, elevation,
					marker=p_lst[i % len(p_lst)],
					linewidth=(5 if i == 0 else 2),
					color=c_lst[i%len(c_lst)](n / 31)
				)
	
	plt.grid()
	plt.axis('equal')
	plt.show()

