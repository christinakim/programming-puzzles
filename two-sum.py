# array_sum.py
"""
You have an array of n elements, and a sum.
Check if any 2 elements in the array sum to the given sum. (Expected time complexity O(n). Use hashing)
"""

# O(n^2)
def array_sum_brute(array, sum):
    for n in array:
        for m in array:
            if n + m == sum:
                return True

    return False

# O(nlogn)
def array_sum_better(array, sum):
    array = sorted(array)
    start = 0
    end = len(array) - 1

    while start < end:
        total = array[start] + array[end]
        if total < sum:
            start += 1
        elif total > sum:
            end -= 1
        else:
            return True

    return False

# O(n)
def array_sum_best(array, sum):
    differences = set()
    for n in array:
        differences.add(sum - n)

    for n in array:
        if n in differences:
            return True

    return False

def main():
    array = [1, 5, 7, 2, 4, 6]
    sum = 9
    assert array_sum_brute(array, sum) == True
    array = [1, 5, 7, 3, 4, 6]
    sum = 15
    assert array_sum_brute(array, sum) == False

    array = [1, 5, 7, 2, 4, 6]
    sum = 9
    assert array_sum_better(array, sum) == True
    array = [1, 5, 7, 3, 4, 6]
    sum = 15
    assert array_sum_better(array, sum) == False

    array = [1, 5, 7, 2, 4, 6]
    sum = 9
    assert array_sum_best(array, sum) == True
    array = [1, 5, 7, 3, 4, 6]
    sum = 15
    assert array_sum_best(array, sum) == False

    print 'All tests pass!'

if __name__ == '__main__':
    main()
