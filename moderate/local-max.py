"""Given an array, find first instance of local maxima ( greater than both the left and right elements in an array )

    mid=(start+end)/2; 
    1. if(A[mid-1]>=A[mid] && A[mid+1]>=A[mid]) then A[mid] is a local minimum. 
    2. else if(A[mid-1]<=A[mid] && A[mid]<=A[mid+1]) end=mid, do recursive search. 
    3. else if(A[mid-1]>=A[mid] && A[mid]>=A[mid+1]) start=mid, do recursive search 
    it is O(logn)

     at least two local minima, choose one

"""

def local_max(n):
    mid = len(n)/2
    if n[mid-1] <= n[mid] and n[mid+1] <= n[mid]:

        return n[mid], mid
    elif n[mid-1] <= n[mid] and n[mid] <= n[mid+1]:

        return local_max(n[mid:])
    elif n[mid-1] >= n[mid] and n[mid] >= n[mid+1]:
        return local_max(n[:mid])
    else:
        return local_max(n[:mid])



def main():
    A = [9,7,7,2,1,3,7,5,4,7,3,3,4,8,6,9]
    print local_max(A)

if __name__ == '__main__':
    main()