    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        len_n = len(nums)
        odd_indexes = [-1]
        for i, n in enumerate(nums):
            if n % 2 == 1:
                odd_indexes.append(i)
        odd_indexes.append(len_n)
        count = 0
        len_o_i = len(odd_indexes)
        for o_i_i in range(1, len_o_i - k):
            count += (odd_indexes[o_i_i] - odd_indexes[o_i_i - 1]) * (odd_indexes[o_i_i + k] - odd_indexes[o_i_i + k - 1])
                
        return count
