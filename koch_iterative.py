import turtle
import time


def koch_iterative(iterations) :
    
    koch_set = "F"# start with f this koch(0)
    for i in range(iterations):#number of k(n) i want to display
        koch_set = koch_set.replace("F","FLFRFLF")       
# first iteration i have zero and this is koch(0) 
#second iteration i remove the f and replace it with FLFRFLF koch(2)
# for third iteration, i remove ech F in the FLFRFLF and add to it FLFRFLF so it expands koch(2) FLFRFLFLFLFRFLFRFLFRFLFLFLFRFLF
    turtle.down()
     for move in koch_set:     # follow the specified moves
        if move == "F":
            turtle.forward(100.0 / (3 ** (iterations - 1))) #forward move length,normalized
        elif move == "L":
            turtle.left(60) # rotate left 60 degrees
        elif move == "R":   
            turtle.right(120) # rotate right 120 degrees
            
koch_iterative(4)
     

#koch_flake = "FRFRF" to show entire snown flake and same of rest