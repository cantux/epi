#!/usr/bin/env python

def brut():
    len_n = len(nums)
    def rec(curr_idx, rem):
        if curr_idx == len_n:
            return 0
        
        used = -sys.maxsize - 1
        if nums[curr_idx] <= rem:
            used = rec(curr_idx + 1, rem - nums[curr_idx]) + 1
        return max(used, rec(curr_idx + 1, rem))
    
    return rec(0, k)

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

