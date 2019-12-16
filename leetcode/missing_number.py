    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         mx = max(nums)
#         mn = min(nums)
        
#         s = set(nums)
        
#         for i in range(mn, mx):
#             if i not in s:
#                 return i
            
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
