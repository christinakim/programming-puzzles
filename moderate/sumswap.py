"""
given two arrays of integers find a pair of values that you can swap to give the arrays the same sum

input = [4,1,2,1,1,2] + [3,6,3,3]
out put = 1,3
"""

def sumswap(n, m):
    sum_n = sum(n)
    sum_m = sum(m)
    
    diff = abs(sum_n - sum_m)
    if diff == 0:
        print 'Nothing to swap'

        return None
    elif diff > sum_n or diff > sum_m:
        print 'Swap not possible'
        return None
    else:
        sorted_n = sorted(n)
        sorted_m = sorted(m)
        x = 0
        y = 0
        while x < len(n) and y < len(m):
            if sorted_n[x] + sorted_m[y] == diff:
                return sorted_n[x],sorted_m[y]
            elif sorted_n[x] + sorted_m[y]> diff:
                y += 1
            else:
                x += 1

def main():
    n = [4,1,2,1,1,2]
    m = [3,6,3,3]
    assert sumswap(n, m) == (1,3)
    
    n = [10,10,10]
    m = [2,3,4,5]
    assert sumswap(n,m) == None
    
    print 'assertions passed!'

if __name__ == '__main__':
    main()