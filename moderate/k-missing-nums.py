"""
finding k missing numbers

if there's one missing:
sum of original - new = missing num

now what if there are two missing num?... three missing num?
        int diffSqr = (int)Math.sqrt(s*s-4*product); // (a-b)^2 = (a+b)^2-4ab
        a = (s+diffSqr)/2;
        b= s-a;
        int [] result = {a,b};
        return result;

"""
from math import sqrt
def missingK(n, arr):
    total = n*(n+1)/2
    m_total = sum(arr)
    miss_num = total - m_total
    prod = 1
    arr_prod = 1
    
    for i in range(1, n+1):
        prod *= i 
    for i in arr:
        arr_prod *= i

    miss_prod = prod/arr_prod

    #(a-b)^2 = (a+b)^2-4ab
    #diffsq = a-b
    #miss_num = a + b
    diffSq = int(sqrt(miss_num**2-(4*miss_prod)))
    a = (diffSq + miss_num)/2
    b = miss_num - a
    return a, b

def missingKSet(n, arr):
    complete = set()
    for i in range(1,n+1):
        complete.add(i)
    missing = set()
    for i in arr:
        missing.add(i)

    missing = complete.difference(missing)

    return list(missing)

def main():
    arr = [i for i in range(1,31)]
    arr.pop()
    arr.pop()

    print missingKSet(30, arr)
    print missingK(30, arr)
if __name__ == '__main__':
    main()
