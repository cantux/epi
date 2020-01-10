def move_zeros(nums):
    len_n = len(nums)
    last_non_zero = 0
    ptr = 0
    while ptr < len_n:
        if nums[ptr] != 0:
            nums[last_non_zero] = nums[ptr]
            last_non_zero += 1
        ptr += 1
    
    while last_non_zero < len_n:
        nums[last_non_zero] = 0
        last_non_zero += 1
        
    return nums
