def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    len_n = len(nums)
    if len_n == 0:
        return 0
    elif len_n == 1:
        return nums[0]
    if len_n > 2:
        nums[2] += nums[0]

        for i in range(3, len_n):
            nums[i] = max(nums[i - 2], nums[i - 3]) + nums[i]

    return max(nums[len_n - 1], nums[len_n - 2])

def test():
    assert rob([]) == 0
    assert rob([1,2,3,1]) == 4
    assert rob([2,7,9,3,1]) == 12
    assert rob([1, 2, 3]) == 4
    assert rob([2]) == 2
    assert rob([1, 2]) == 2

if __name__ == "__main__":
    test()
