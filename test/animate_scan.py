#!/usr/bin/env python3

import ast
import collections
import sys
import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

from cc_pathlib import Path

import cloudy.loader

# m_map = cloudy.loader.load_pcd(Path(sys.argv[1]))
m_map = Path("test.pickle.br").load()

a_arr = np.hstack([np.array(m_map[0][i])[:,0] for i in m_map[0]])
e_arr = np.hstack([np.array(m_map[0][i])[:,1] for i in m_map[0]])

fig = plt.figure()

plt.grid()
plt.axis("equal")

plt.plot(a_arr, e_arr, alpha=0.3)
line, = plt.plot(a_arr, e_arr)

m = 32
n = len(a_arr) // m

def func(i) :
	print(i%n)
	line.set_xdata(a_arr[m*(i%n):m*((i%n)+8)])
	line.set_ydata(e_arr[m*(i%n):m*((i%n)+8)])
	return line,

# x = np.arange(0, 2*np.pi, 0.01)
# line, = plt.plot(x, np.sin(x))s

# def func(i) :
# 	print(i)
# 	line.set_ydata(np.sin(x + i / 50))  # update the data.
# 	return line,

_ = ani.FuncAnimation(fig, func, interval=10, blit=True, save_count=10)

plt.show()
