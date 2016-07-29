"""http://stackoverflow.com/questions/17119116/how-many-ways-can-you-insert-a-series-of-values-into-a-bst-to-form-a-specific-tr
"""
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

# for a given number a and a list L, this functions returns the left tree (a list) and the right tree (a list)
def TreeGenerator(seq): 
    root = seq[0]
    seq = seq[1:]
    left_tree = []
    right_tree = []
    for i in seq:
        if i<root:
           left_tree.append(i)
        else:
           right_tree.append(i)
    solution = [left_tree,right_tree]
    return(solution)

def bstPermutation(seq):
    if len(seq) == 0 or len(seq) == 1: 
        return 1
    else:
        t = TreeGenerator(seq)
        m = len(t[0])
        n = len(t[1])
        return nCr(m + n, n) * bstPermutation(t[0]) * bstPermutation(t[1])

def answer(seq):
    return str(bstPermutation(seq))
              

print TreeGenerator([5, 2, 9, 1, 8])
print TreeGenerator([2, 1])
print TreeGenerator([5, 9, 8, 2, 1])

"""
Test cases
==========

Inputs:
    (int list) seq = [5, 9, 8, 2, 1]
Output:
    (string) "6"

Inputs:
    (int list) seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output:
    (string) "1"
"""
        