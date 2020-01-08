# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
def findMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    len_n = len(nums)
    ones_c = [0] * len_n
    zeros_c = [0] * len_n
    zeros_c[0] = 1 if nums[0] == 0 else 0
    ones_c[0] = 1 if nums[0] == 1 else 0
    for i, n in enumerate(nums[1:], 1):
	if n == 0:
	    zeros_c[i] = zeros_c[i - 1] + 1
	    ones_c[i] = ones_c[i - 1]
	else:
	    zeros_c[i] = zeros_c[i - 1]
	    ones_c[i] = ones_c[i - 1] + 1
	
    max_found = 0
    dct = {}
    dct[0] = -1
    for i in range(len_n):
	diff = zeros_c[i] - ones_c[i]
	if diff in dct:
	    max_found = max(max_found, i - dct[diff])
	else:
	    dct[diff] = i
    return max_found

def findMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    len_n = len(nums)
	
    ones_c = 0
    zeros_c = 0
    
    max_found = 0
    
    dct = {}
    dct[0] = -1
    for i in range(len_n):
	if nums[i]:
	    ones_c += 1
	else:
	    zeros_c += 1
	diff = zeros_c - ones_c
	if diff in dct:
	    max_found = max(max_found, i - dct[diff])
	else:
	    dct[diff] = i
    return max_found
