#!/usr/bin/env python

# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

# Since the answer may be large, return the answer modulo 10^9 + 7.

def brute_force(arr):
    len_a = len(arr)

    res = 0
    for i in range(len_a):
        for j in range(i + 1, len_a):
            res += min(arr[i:j])
            res = res % ((10 ** 9) + 7)
    return res

# stack solution
# find PLE and NLE
# that means that any combination between
# i is the minimum value between ple[i] and nle[i] 
# between 2 and 4 there are 2, 3, 4, 2,3, 3,4, 2,3,4
# there ar 3, 23, 34, 2,3,4
# given n numbers, how many subsets include the item x
def better(arr):
    mins_left = []
    mins_right = []


def test():
    assert brute_force([3,1,2,4]) == 17

if __name__ == "__main__":
    test()

