import math
def ternary (n, pos):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 3)
            if r > 0:
                nums.append(r)   
        return nums

def answer(x):
    unweighted = ternary(x)
    weights = []
    for i in range(len(unweighted)):
        if unweighted[i] > 1:
            if i +1 > len(unweighted):
                unweighted[i] = unweighted[i] - 3
                unweighted[i+1] = unweighted[i+1] + 1
            else:
                unweighted.append(1)
    for j in range(len(unweighted)):
        if unweighted[j] == 1:
            weights.append('R')
        if unweighted[j] == 0:
            weights.append('-')
        if unweighted[j] == -1:
            weights.append('L')
    
   
    