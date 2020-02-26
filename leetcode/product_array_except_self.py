    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # brute force
        len_n = len(nums)
#         res = [1] * len_n
#         times = lambda x,y: x * y
#         for i in range(len_n):
#             res[i] = reduce(times, nums[:i - 1]) * reduce(times, nums[i+1:])
            
#         return res

        times_left = [1]
        for i in range(1, len_n):
            times_left.append(times_left[-1] * nums[i - 1])
            
        times_right = [1] * len_n
        for j in range(len_n - 1)[::-1]:
            times_right[j] = times_right[j + 1] * nums[j + 1]
            
        # print "times_left: ", times_left
        # print "times_right: ", times_right
        
        ans = [1] * len_n
        for i in range(len_n):
            ans[i] = times_left[i] * times_right[i]
            
        return ans
    
