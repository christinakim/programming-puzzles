"""
o(nlogn + mlogm)
"""
import sys

def smallest(n, m):
    n = sorted(n)
    m = sorted(m) 

    ptr_n = 0
    ptr_m = 0

    min_diff = sys.maxsize
    while ptr_m < len(m) and ptr_n < len(n):
        print min_diff
        temp = abs(n[ptr_n] - m[ptr_m])
        if temp < min_diff:
            min_diff = temp
        if n[ptr_n] > m[ptr_m]:
            ptr_m += 1
        else:
            ptr_n += 1

    return min_diff


def main():
    n = [13,14,11,2] 
    m = [23,127,235,19,8]
    assert smallest(n,m) == 3

if __name__ == '__main__':
    main()