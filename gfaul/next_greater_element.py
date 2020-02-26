#!/usr/bin/env python

# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
# If it does not exist, output -1 for this number.

def fnc(nums1, nums2):
    res = []
    len_n1 = len(nums1)
    s = []
    for i in range(len_n1):
        while s and nums2[s[-1]] < nums1[i]:

    return None

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

