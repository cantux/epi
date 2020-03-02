def singleNonDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # binary search for the first index that does not have the value
    
    # now imagine we have 5 elements
    # 11 2 33 -> nums[mid=2]-> 2
    #    ^
    
    # how about example
    # 11 2 33 44 -> 7 elements-> 7// 2 = 3
    #      ^
    
    # 11 22 3 44 -> 7 elements 7 // 2 = 3
    #     ^
    len_n = len(nums)
    lo, hi = 0, len_n - 1
    
    while lo < hi:
	mid = lo + ((hi - lo) // 2)
	if mid % 2 == 1:
	    mid -= 1
	if nums[mid + 1] == nums[mid]:
	    lo = mid + 2
	else:
	    hi = mid
    return nums[lo]
