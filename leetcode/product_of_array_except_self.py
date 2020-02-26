    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
        arr = [1] * len(nums)
        pi = pj = 1

        for i in range(len(nums)):
            j = -1-i

            arr[i]*=pi; arr[j]*=pj
            pi *= nums[i]; pj *= nums[j]        
                    
        return arr
    
    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        ret = [1] * len_nums
        
        ret[0] = 1
        for i in range(1, len_nums):
            ret[i] = nums[i - 1] * ret[i - 1]
                
        prev = 1
        for i in reversed(range(len_nums)): 
            ret[i] = ret[i] * prev
            prev *= nums[i]
            
        return ret
