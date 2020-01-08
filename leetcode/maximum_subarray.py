# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def max_subarray(nums):
    len_n = len(nums)
    
    sums = [nums[0]] + ([0] * len_n)
    
    for i in range(1, len_n):
        sums[i] = sums[i - 1] + nums[i]
    
    current_max = -sys.maxsize - 1
    min_until = 0
    for i, n in enumerate(nums):
        current_max = max(current_max, sums[i] - min_until)
        min_until = min(min_until, sums[i])

    return current_max

def max_subarray_inplace(nums):
    len_n = len(nums)
    
    for i in range(1, len_n):
        nums[i] = nums[i - 1] + nums[i]
    
    current_max = -sys.maxsize - 1
    min_until = 0
    for i, n in enumerate(nums):
        current_max = max(current_max, nums[i] - min_until)
        min_until = min(min_until, nums[i])

    return current_max
def test():
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6

if __name__ == "__main__":
    test()
