def subarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    len_n = len(nums)
    prefix_sum = [0] * (len_n + 1)
    prefix_sum[0] = 0
    for i in range(1, len_n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
    count = 0 
    for i in range(len_n):
        for j in range(i + 1, len_n + 1):
            if prefix_sum[j] - prefix_sum[i] == k:
                count += 1
                
    return count

def subArraySum_o1space(nums, k):
    len_n = len(nums)
    count = 0
    for i in range(len_n):
        curr_sum = 0
        for j in range(i, len_n):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1
    return count


    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        len_n = len(nums)
        sum_count_dct = defaultdict(int)
        sum_count_dct[0] = 1

        count = 0 
        curr_sum = 0
        for i in range(len_n):
            curr_sum += nums[i]
            curr_target = curr_sum - k
            if curr_target in sum_count_dct:
                count += sum_count_dct[curr_target]
            sum_count_dct[curr_sum] += 1
        return count
def test():
    assert subArraySum_o1space([1, 1, 1], 2) == 2


if __name__ == "__main__":
    test()

