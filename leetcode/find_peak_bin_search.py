
def find_peak(nums):
    len_nums = len(nums)
    l, r = 0, len_nums - 1

    while l < r:
	m = l + ((r - l) // 2);
	if nums[m] > nums[m + 1]:
	    r = m
	else:
	    l = m + 1
    
    return l
