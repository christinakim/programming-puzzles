"""
input [1,2,4,7,10,11,7,12,6,7,16,18,19]
output (3,9)

smallest subseq that if sorted would result in input being sorted
"""

import sys

def subsort(n):
    left = n[:len(n)/2]
    right = n[len(n)/2:]
    left_index = len(n)/2 -1
    right_index = len(n)/2
    left_max = left[-1]
    right_min = right[0]

    for i in range(len(left)):
        left[i] 




def main():
    n = [1,2,4,7,10,11,7,12,6,7,16,18,19]


    assert subsort(n) == (3,9)

if __name__ == '__main__':
    main()