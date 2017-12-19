# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:57:58 2017

@author: christian
"""
# agentframework.py
import random
class Agent():
    
     def __init__(self, environment):
                self.x = random.randint(0,99)  
                self.y = random.randint(0,99)       
                self.environment = environment
                self.store = 0                 
       
     def move(self):
                if (random.random() < 0.5):
                        self.x = self.x + 1
                else:
                        self.x = self.x - 1
                    

     def eat(self):
          if self.environment[self.y][self.x] > 10:
              self.environment[self.y][self.x] -= 10
              self.store += 10        
