"""
For example, if the array was [1,4,1] you could perform the operations as follows:

Send a rabbit from the 1st car to the 0th: increment x[0], decrement x[1], resulting in [2,3,1]
Send a rabbit from the 1st car to the 2nd: increment x[2], decrement x[1], resulting in [2,2,2].

All the elements are of the array are equal now, and you've got a strategy to report back to Beta Rabbit!

Note that if the array was [1,2], the maximum possible number of equal elements we could get is 1, as the cars could never have the same number of rabbits in them. 

Write a function answer(x), which takes the array of integers x and returns the maximum number of equal array elements that we can get, by doing the above described command as many times as needed. 
Test cases
==========

Inputs:
    (int list) x = [1, 4, 1]
Output:
    (int) 3

Inputs:
    (int list) x = [1, 2]
Output:
    (int) 1

    
    sorted_x = sorted(x)
    start = 0
    end = len_x - 1

    while start != end:
        need = goal - sorted_x[start]
        for i in range(need):
            if sorted_x[end] > goal:
                sorted_x[end] = sorted_x[end] - 1
                sorted_x[start] = sorted_x[start] + 1
            else:
                end = end - 1
    
"""

def answer(x):
	total = sum(x)
	goal = round(total/len(x))

	if len(x) * goal == total:
		return len(x)
	else:
		return len(x) - 1