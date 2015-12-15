def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
 

    if len(nums1) == 1:
    	return nums1[0]
    elif len(nums2) == 1:
    	return nums2[0]
    
    nums1A = nums1[:len(nums1)//2]
    nums2B = nums2[:len(nums1)//2]

    if nums1A[len(nums1A) - 1] > nums2B[len(nums2B) - 1]:
        findMedianSortedArrays(nums1A, nums2)
    elif nums1[len(nums2)/2] < nums2[len(nums2)/2]: 
    	findMedianSortedArrays(nums1, nums2B) 

def main():
	n1 = [2, 4, 6, 8, 10, 11]
	n2 = [1, 3, 5, 7, 9]
	assert findMedianSortedArrays(n1, n2) == 6

if __name__ == '__main__':
	main()