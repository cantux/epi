    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: nt
        """
        if not nums: return 0
        len_n = len(nums)
        sums = [0] * len_n
        sums[0] = nums[0]
        for i in range(1, len_n):
            sums[i] += sums[i - 1] + nums[i]

        # imagine there is a solution between i and jth index where i < j
        # then, sums[j] - sums[i] should be equal to target k
        # sums[j] = sums[i] + k
        # look for the index of the sum_j from the map of sums.
        # when we find an index, update the maximum range by subtracting found index from the current index. (it is gauranteed that the found index will be bigger)
        
        # Because of negatives, there are indeces that yield to the same sum. When we create the map below, we are overriding the previous indeces that yield to the same sum. This is not a problem since we are always looking for the maximum range and start from 0 and move towards it in the next loop, but we have to watch out for the following special case:
            # imagine target is k. sum at the current index i is also k and there is a sum 2k on the jth index.
            # we have to record i to be a possible range from 0 to i or check if j - i is larger than i.
        val_idx_map = {s: i for i, s in enumerate(sums)}

        max_range = 0
        for i, n in enumerate(nums):
            if sums[i] == k:
                max_range = max(max_range, i + 1)
            if (k + sums[i]) in val_idx_map:
                max_range = max(max_range, val_idx_map[k + sums[i]] - i)
                
        return max_range
