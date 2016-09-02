# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    if len(A) == 0:
        return -1
    if len(A) == 1:
        return 0
    sum_left = 0
    sum_right = sum(A[1:])
    
    if sum_left == sum_right:
        return 0
    for i in range(len(A)-1):
        sum_left += A[i]
        sum_right -= A[i+1]
        
        if sum_left == sum_right:
            return i+1
        
        
    return -1