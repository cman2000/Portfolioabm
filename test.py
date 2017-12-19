# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:52:16 2017

@author: christian
"""


#environment.append(rowlist)
#rowlist.append(value)
#rowlist = []	
#environment = []

f = open('datain.txt') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:	# A list of rows
    rowlist = []
    for value in row:	# A list of value
        rowlist.append(value)    	        
    environment.append(rowlist)   
#print(environment) # Floats
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
f.close() # Don't close until you are done with the reader;
        # the data is read on request.