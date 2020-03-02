ortedSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    len_n = len(nums)
    s = []
    next_small = [-1] * len_n
    for i in range(len_n):
        while s and nums[s[-1]] > nums[i]:
            next_small[s.pop()] = i

        s.append(i)

    start = -1
    for n_s_i in range(len_n):
        if next_small[n_s_i] != -1:
            start = n_s_i
            break


    prev_larger = [len_n] * len_n
    s = []
    for i in range(len_n):
        while s and nums[s[-1]] <= nums[i]:
            s.pop()
        prev_larger[i] = s[-1] if s else len_n
        s.append(i)

    end = len_n
    for p_l_i in reversed(range(len_n)):
        if prev_larger[p_l_i] != len_n:
            end = p_l_i
            break

    return 0 if start == -1 or end == len_n else end - start + 1
