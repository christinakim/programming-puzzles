"""
return all subsets of a set 

combinations problem r fun 
"""

def powerset(n, l = -2,memo = {}):
    if l == -2:
        l = len(n)
    if l == 0:
        memo[0] = 1 
        return 1
    if l == 1:
        memo[1] = len(n)
    else:
        combo = [powerset(n, i, memo) for i in range(len(n)) if l - i >= 0]
        memo[n] = len(combo)
        return memo[n]


def main():
    s = [1,2,3]
    print powerset(s)

if __name__ == '__main__':
    main()