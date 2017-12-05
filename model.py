# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random #imports function from random module
import operator # imports function used to find max on second part to list (1)
import matplotlib.pyplot # imports chart plotting function

#set up variables
num_of_agents = 10 # creates new variable with value of 10
num_of_iterations = 100 # creates new variable with value of 100

#y0 = random.randint(0,99) # Make a y variable. using random number between 0 and 99
#x0 = random.randint(0,99) # Make a x variable.using random number between 0 and 99
agents = []#creates alist called agents

for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])#appends two random coordinates values between 0 and 99 to list agents, removes need for x and y variables


for j in range(num_of_iterations): # moves all agents by variable ammount (nested loop)
    for i in range(num_of_agents):#loops through and creates coordinate creation code by number of agents 
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100 # changes the boundary limit
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
    #show both values on one line   
    #print (agents [i] [0],agents[i] [1]) 
         
    
    
    
#answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
#print(answer)
#print(max(agents))
#print(max(agents, key=operator.itemgetter(1)))
## used to find max on second part to list (1)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents): # display all agents
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()