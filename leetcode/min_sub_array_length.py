def minSubArrayLen(self, s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    # move a window
    if not nums: return 0
    len_n = len(nums)
    curr_s = 0
    left, right = 0, 0
    min_found = sys.maxsize
    while right < len_n:
	curr_s += nums[right]
	while curr_s >= s:
	    min_found = min(min_found, right - left + 1)
	    curr_s -= nums[left]
	    left += 1
	    
	right += 1
	
    return min_found if min_found !=sys.maxsize else 0
