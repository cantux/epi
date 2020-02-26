
# works only for unique elements

# this is a subset problem of two sum.
# implementation below is asymptotically upper bound by nlgn.
# if the elements are given in sorted order and we ask wether if two sum exists following solution is O(1) space alternative.
Sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_to_idx = {v: i for i, v in enumerate(nums)}
        nums.sort()
        sorted_to_past = {i: nums_to_idx[n] for i, n in enumerate(nums)}
        
        len_n = len(nums)
        left, right = 0, len_n - 1
        
        while left <= right:
            curr = nums[left] + nums[right]
            if curr == target:
                found = [left, right]
                break
            elif curr < target:
                left += 1
            else:
                right -= 1
        
        return [sorted_to_past[found[0]], sorted_to_past[found[1]]]


