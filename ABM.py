# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

y0 = 50
x0 = 50
x1 = 50
y1 = 50

if random.random() < 0.5:
    y0 += 1
    x0 += 1
else:
    y0 -= 1
    x0 -= 1

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5

print(y0, x0) 
print(answer)