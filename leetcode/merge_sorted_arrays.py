

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	"""
	Do not return anything, modify nums1 in-place instead.
	"""
	

	ptr_top_arr = m - 1
	ptr_bot_arr = n - 1
	ptr_end = m + n - 1

	while ptr_top_arr >= 0 and ptr_bot_arr >= 0:
		if nums1[ptr_top_arr] >= nums2[ptr_bot_arr]:
			nums1[ptr_end] = nums1[ptr_top_arr]
			ptr_top_arr -= 1
		else:
			nums1[ptr_end] = nums2[ptr_bot_arr]
			ptr_bot_arr -= 1
		ptr_end -= 1
	
	while ptr_bot_arr >= 0:
		nums1[ptr_end] = nums2[ptr_bot_arr]
		ptr_bot_arr -= 1
		ptr_end -= 1
