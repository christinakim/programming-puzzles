"""
magic index 

a magic inex in an array is defined to be an index such that a[i] = i given a sorted array of distinct integers

write a method to find a magic index, if one exists, in array a
"""
def find_magic_brute(ints): 
    for i in range(len(ints)):
        if i == ints[i]:
            return i

    return -1

# if it sorted and distincttho
def find_magic_binary_search(ints, start = 0, end = -1):
    if end == -1:
        end = len(ints) - 1 
    if end < start:
        return -1

    mid = (start+end)/2
    if ints[mid] == mid:
        return mid
    elif ints[mid] > mid:
        return find_magic_binary_search(ints, start, mid - 1)
    elif ints[mid] < mid:
        return find_magic_binary_search(ints, mid + 1, end)

#if it not distinct but still sorted tho
#can stil use binary search just modified
def magic_fast(ints, start=0, end = -1):
    if end == -1:
        end = len(ints) - 1
    mid_index = (start+end)/2
    mid_val = ints[mid] 

    if end < start:
        return - 1
    mid_index = min(mid_val, mid_index)
    left = magic_fast(ints, start,mid_index)
    if left >= 0:
        return left
    
    mid_index = max(min_val, mid_index - 1)
    right = magic_fast(ints, mid_index + 1, end)
    return right


def main():
    n = [-20,1,2,20,30,25,40]
    assert find_magic_binary_search(n) == 1 or find_magic_binary_search == 2
    
if __name__ == '__main__':
    main()