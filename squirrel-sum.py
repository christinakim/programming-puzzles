# Enter your code here. Read input from STDIN. Print output to STDOUT
#00 11 2 10 02

import math 
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def closest_nut(squirrel_pos, nuts_pos):
    #returns tuple of closest nut location
    closest_nut = nuts_pos[0]
    for i in range(1,len(nuts_pos)):
        if distance(squirrel_pos, closest_nut) > distance(squirrel_pos, nuts_pos[i]):
            closest_nut = nuts_pos[i]
    return closest_nut

def steps_to(squirrel_pos, next_pos):
    sum_steps = abs(next_pos[0]-squirrel_pos[0]) 
    sum_steps = sum_steps+ abs(next_pos[1]-squirrel_pos[1])
    return sum_steps
    
def steps():
    #breaking inputs into variables
    inputs = raw_input().split()
    squirrel_pos = tuple([int(i) for i in str(inputs[0])])
    tree_pos = tuple([int(i) for i in str(inputs[1])])
    num_nuts = int(inputs[2])
    #creating a list of tuples of nut locations
    nuts_pos = []
    for j in range(3,len(inputs)):
        nuts_pos.append(tuple(int(i) for i in str(inputs[j])))
   
    step_counter = 0
    
    while num_nuts != 0:
        print step_counter
        next_pos = closest_nut(squirrel_pos, nuts_pos)
        step_counter = steps_to(squirrel_pos, next_pos) + step_counter
        squirrel_pos = next_pos
        print step_counter
        print "hello"
        print steps_to(squirrel_pos, tree_pos)
        step_counter = steps_to(squirrel_pos, tree_pos) + step_counter
        squirrel_pos = tree_pos
        num_nuts = num_nuts - 1
        print step_counter
        
    print int(step_counter)

steps()