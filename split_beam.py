#!/usr/bin/env python3

import math

from cc_pathlib import Path

import matplotlib.pyplot as plt

b_lst = list()

def split_azimuth(ae_lst) :
	b = None
	c_lst = list()
	for a, e in ae_lst :
		if b is not None and (b - a) > 1.0 :
			r_lst, l_lst = split_beam(c_lst)
			b_lst.append(r_lst)
			b_lst.append(l_lst)
			c_lst = list()
		c_lst.append([a, e])
		b = a
	r_lst, l_lst = split_beam(c_lst)
	b_lst.append(r_lst)
	b_lst.append(l_lst)
	return b_lst
	
def split_beam(c_lst) :
	r_lst = c_lst[::2]
	l_lst = c_lst[1::2]
	return r_lst, l_lst
	

ae_lst = [
	[float(a), float(e)]
	for a, e in Path("azimuth_elevation.tsv").load()
]

b_lst = split_azimuth(ae_lst)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for c_lst in b_lst :
	ax.plot(
		[math.cos(e) * math.cos(a) for a, e in c_lst],
		[math.cos(e) * math.sin(a) for a, e in c_lst],
		[math.sin(e) for a, e in c_lst],
	)
plt.show()
		
