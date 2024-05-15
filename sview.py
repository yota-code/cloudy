#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


from cc_pathlib import Path

txt = Path("uniform_snap_10Hz.tsv").read_text()

u = np.array([[float(i) for i in line.split('\t')] for line in txt.splitlines()])
print(u.shape)

plt.plot(u[:,0], u[:,1])
plt.show()

