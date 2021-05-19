# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:22:16 2021

@author: jyfxx
"""

import csv
import matplotlib.pyplot as mbp
import numpy as np
import drunkframework
import random

environment = []
density = np.mat(np.zeros((300,300)))
drunk = []
namelist = list(range(10,260,10))
f = open ("drunk.txt", newline="")
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for values in row:
        rowlist.append(values)
    environment.append(rowlist)
f.close()

n = np.array(environment)
a, b = np.where(n == 1)
num_of_drunks = 25

for i in range(num_of_drunks):
    index = random.choice(range(len(a)))
    x = b[index]
    y = a[index]
    name = random.choice(namelist)
    namelist.remove(name)
    img = drunkframework.Drunk(environment, x, y)
    drunk.append(img)
    while int(img.environment[img.y][img.x]) != int(name):
        drunk[i].move()
        density[img.y, img.x] += 1
        if int(img.environment[img.y][img.x]) == int(name):
            print('break')
            break

mbp.subplot(2,2,1) 
mbp.xlim(0, 300)
mbp.ylim(0, 300)
for i in range(num_of_drunks):
      mbp.scatter(drunk[i].x,drunk[i].y)	
mbp.imshow(environment)
mbp.subplot(2,2,2) 
mbp.xlim(0, 300)
mbp.ylim(0, 300)
mbp.imshow(density)
mbp.colorbar()

with open("file.txt", "w") as output:
    output.write(str(density.tolist()))
