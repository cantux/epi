    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:        
        res = []
        len_n = len(nums)
        def bt(curr, curr_res, curr_lst):
            if curr_res >= 100:  
                return
            elif curr_res < 100:
                res.append(curr_lst)
            for i in range(curr, len_n):
                curr_lst.append(nums[i])
                bt(i + 1, curr_res * nums[i], curr_lst[:])
                curr_lst.pop()
        bt(0, 1, [])
        print(res)
        return len(res) - 1
