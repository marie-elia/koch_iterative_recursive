# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 00:23:02 2019

@author: marie
"""

from turtle import Screen, Turtle
import time
#recursive algorithm from slides
def koch(n):

    'returns directions for drawing curve Koch(n)'
    if n==0:
        return 'F'
    # recursive step: get directions for Koch(n-1)
    tmp = koch(n-1)
    # use them to construct directions for Koch(n)
    return tmp+'L'+tmp+'R'+tmp+'L'+tmp

start=time.time()#start time before calling the function
koch(11)
end=time.time()#end time after calling the function

print("Recursive time")
print(end-start) #print difference in time
print()


def koch_iterative(iterations) :
    
    koch_set = "F"# start with f this koch(0)
    for i in range(iterations): #number of k(n) i want to display
        koch_set = koch_set.replace("F","FLFRFLF")
        
s=time.time()#start time for iterative function
koch_iterative(11)
e=time.time()#end time for iterative function
print("Iterative time")
print(e-s) #print difference in time
