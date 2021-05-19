# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:07:32 2021

@author: jyfxx
"""

import random

class Drunk():
    def __init__(self, environment, x, y):
        self.y = y
        self.x = x      
        self.environment = environment

# used for exam each step going when test:      
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y) + ", name=" + str(self.name) + ", env=" + str(self.environment[self.x][self.y]) +", store=" + str(self.store)
   

    def move(self):
            if random.random() < 0.5:
                self.y = (self.y + 1) % 300
            else:
                self.y = (self.y - 1) % 300
    
            if random.random() < 0.5:
                self.x = (self.x + 1) % 300
            else:
                self.x = (self.x - 1) % 300
    




        

