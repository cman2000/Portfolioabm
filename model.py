# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 
import random # imports relevant libraries
import operator
import matplotlib.pyplot
import agentframework
import csv

f = open('datain.txt') # opens csv file from directory
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) # reads csv and ensures any non mueric characters quoted
environment = [] #creates empty list to hold all data
for row in reader:	# A list of rows
    rowlist = [] #creates empty list for rows
    for value in row:	# A list of value
        rowlist.append(value)  #move row values to row list  	        
    environment.append(rowlist)   # append row lists to environment list
#print(environment) # Floats
matplotlib.pyplot.imshow(environment) #use library to display raster values from environment list 
matplotlib.pyplot.show()
f.close() # closes reader 
        

def distance_between(agent0, agent1): #new function created to call pythhagorus calc for all looped agents
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

  
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
        agents.append(agentframework.Agent(environment))

# Move the agents.

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()       

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)
               