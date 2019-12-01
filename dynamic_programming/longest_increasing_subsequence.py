import sys
import bisect
from collections import deque

def lis(nums):
#         	smaller_item_loc = bisect.bisect_right(nums[0:i], nums[i])
    len_nums = len(nums)
    val_dp = [1] * len_nums
    idx_dp = [-1] * len_nums
    curr_max_loc = 0
    curr_max = -sys.maxint - 1
    for i in range(len_nums):
        for j in reversed(range(i)):
            if nums[j] < nums[i]:
        	curr_count = val_dp[j] + 1
	        idx_dp[i] = j
        	val_dp[i] = curr_count
	        if curr_max < curr_count:
        	    curr_max = curr_count
	            curr_max_loc = i
                break
        print "val_dp: ", val_dp
        print "curr_max: ", curr_max
        print "curr_max_loc: ", curr_max_loc

	
    # construct a solution
    print "idx_dp: ", idx_dp
    ret = deque([])
    curr = curr_max_loc
    while curr > 0:
	ret.appendleft(nums[curr])
	curr = idx_dp[curr]
    print ret

    return curr_max

def test():
    assert lis([10,9,2,5,3,7,101,18]) == 4

if __name__ == "__main__":
    test()

