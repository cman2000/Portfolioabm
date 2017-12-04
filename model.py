# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random #imports from random module

#set up variables
y0 = random.randint(0,99) # Make a y variable. using random number between 0 and 99
x0 = random.randint(0,99) # Make a x variable.using random number between 0 and 99

# Random walk one step on y.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
 # Random walk one step on x.   
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
#show both values on one line   
print (y0, x0) 
  
#repeat step number twice    
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1    
    
print (y0, x0)




#set up variables for second agent
y1 = 50 # Make a y variable.
x1 = 50 # Make a x variable.

# Random walk one step on y.
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
 # Random walk one step on y.   
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
#show both values on one line   
#print (y1, x1) 
  
#repeat step number twice    
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1    
    
#print (y1, x1)

    
