    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        # decompose the problem a bit, try to see if we can word or paraphrase it
        # so that problem is easier/reduced or partitioned.
        # find the missing elements in a given range 
        # I think we can try to insert the given range 
        
        # inputs can be negative.
        # is the given list sorted? if not, first thing I should do is to sort it.
        # can the elements in the input list exceed these ranges? I could add a quick check after sort.
        # can there be duplicate elements?
        
        # there is no beautiful way to visualize this.
        # we are just going to have to invent an algorithm and improve it.
        
        # one solution could be to iteratively go through the array,
        # compare i and i - 1th elements
        
        # complexity
        # n * (check(O(1)) + insert-> append to a list -> O(1))
        # pseudo code
            # for n elements check
                # if they have a gap, try to insert
                    # get the v_s + 1th and v_e - 1th
                        # if they are equal just print it
                        # else put an arrow between them
                # else move along
        # test cases 
        
        # implementation
        nums.sort()
        sm = 0
        for n in nums:
            if n < lower:
                sm += 1
        for n in nums[::-1]:
            if n > upper:
                lg += 1
        nums = [lower -1] + nums[sm:-lg] + [upper + 1]
        
        ret = []
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]: 
                continue
            
            gap = nums[i - 1] - nums[i]
            if gap == 1: 
                continue
            elif gap == 2:
                ret.append(str(nums[i - 1] + 1)
            else:
                ret.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))
        return ret
