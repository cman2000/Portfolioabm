# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random #imports from random module
import operator # function used to find max on second part to list (1)
import matplotlib.pyplot #chart plotting

agents = []#creates alist called agents
#set up variables
#y0 = random.randint(0,99) # Make a y variable. using random number between 0 and 99
#x0 = random.randint(0,99) # Make a x variable.using random number between 0 and 99
agents.append([random.randint(0,99),random.randint(0,99)])#appends values to list agents


# Random walk one step on y.
if random.random() < 0.5:
    agents [0] [0] += 1
else:
    agents [0] [0] -= 1
 # Random walk one step on x.   
if random.random() < 0.5:
    agents [0] [1] += 1
else:
    agents [0] [1] -= 1
#show both values on one line   
#print (agents [0] [0],agents[0] [1]) 
  
#repeatstep numbertwice    
if random.random() < 0.5:
    agents [0] [0] += 1
else:
    agents [0] [0] -= 1
    
if random.random() < 0.5:
    agents [0] [1] += 1
else:
    agents [0] [1] -= 1    
    
print (agents[0] [0],agents[0] [1])



#set up variables for second agent
y1 = random.randint(0,99) # Make a y variable. using random number between 0 and 99
x1 = random.randint(0,99)# Make a y variable. using random number between 0 and 99
agents.append([y1,x1])# add to list

# Random walk one step on y.
if random.random() < 0.5:
    agents [1] [0] += 1
else:
    agents [1] [0] -= 1
 # Random walk one step on x.   
if random.random() < 0.5:
    agents [1] [1] += 1
else:
    agents [1] [1] -= 1
#show both values on one line   
#print (y1, x1) 
  
#repeat step number twice    
if random.random() < 0.5:
    agents [1] [0] += 1
else:
    agents [1] [0] -= 1
    
if random.random() < 0.5:
    agents [1] [1] += 1
else:
    agents [1] [1] -= 1    
    
print (agents[1] [0],agents[1] [1])
#print (y1, x1)
    
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
#print(answer)
#print(max(agents))
print(max(agents, key=operator.itemgetter(1)))
## used to find max on second part to list (1)

matplotlib.pyplot.ylim(0, 99) #presents agent coordinates on scatter chart from library
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))#Ensures the most eastly point is always red
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()