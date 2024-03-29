# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:46:19 2021

@author: jyfxx
"""

import random


class Agent():
   
    def __init__(self, environment, agents, y, x):
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
       
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x 
            
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.speed = 0
      
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y) + ", store=" + str(self.store)
    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store = self.store + 10 + self.speed
        if  self.store > 4000:
            self.speed += 100 

            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
    

   