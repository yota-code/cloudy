#!/usr/bin/env python3

import ast
import collections
import sys

import numpy as np
import matplotlib.pyplot as plt

from cc_pathlib import Path

def open_pcd(pth) :
	h_lst = ['x', 'y', 'z', 'reflectance', 'azimuth', 'elevation', 'range', 'line_number', 'detector_number']
	m_map = collections.defaultdict(list)
	is_data = False
	for line in pth.read_text().splitlines() :
		if line == 'DATA ascii' :
			is_data = True
			continue
		if is_data :
			v_lst = [ast.literal_eval(v) for v in line.split()]
			assert len(v_lst) == len(h_lst)
			for h, v in zip(h_lst, v_lst) :
				m_map[h].append(v)
			
	for h in m_map :
		m_map[h] = np.array(m_map[h])

	return m_map
    
if __name__ == '__main__' :
	p_lst = ['+', 'x']
	for arg in sys.argv[1:] :
		m_map = open_pcd(Path(arg))
		plt.scatter(m_map['x'], m_map['z'], marker=p_lst.pop(0))
	plt.show()
	plt.grid()
