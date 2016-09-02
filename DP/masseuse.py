"""
the masseuse

receives back to back appts and needs to figure out which one to accepts
needs a 15 min break between appointments 

input = 
[30, 15, 60, 75, 45, 15, 45]
30 75 45
output = 180 min => [30, 60, 45, 45]
"""

def scheduler(n, i =0, memo = {}):
    if i >= len(n):
        memo[i] = 0
        return 0
    if i not in memo:
        best_with = n[i] + scheduler(n, i + 2, memo)
        best_wo = scheduler(n, i+1, memo)
        memo[i] = max(best_with, best_wo)
    return memo[i]
        



#
#this is o(n) time and o(1) space
#iterative soln
#"""

def sched_itr(n):
    i = 0
    j = 0
    for k in range(len(n)):
        best_w = n[k] + i
        best_wo = j
        current = max(best_w, best_wo)
        i = j
        j = current
    return current


def main():
    print scheduler([30, 15, 60, 75, 45, 15, 15, 45])

    print scheduler([1, 2, 3], 0, {})

    print scheduler([5, 1, 2, 6], 0, {})

    print scheduler([5, 1, 2, 6, 20, 2], 0, {})
    print sched_itr([30, 15, 60, 75, 45, 15, 15, 45])

if __name__ == '__main__':
    main()