#!/usr/bin/env python

import sys

def brut_largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    # I want to first breakdown the problem a bit and introduce some terms that I will be using 
    
    # I am thinking maybe the best way to start is to describe a solution that we will reach by running the algorithm
    # we are about to invent
    
    # a solution will be between an _start and an _end index s.t 
    if not heights: return 0
    len_a = len(heights)
    if len_a == 1: return heights[0]
    
    res = [min(heights[_start:_end]) * (_end - _start) for _start in range(1, len_a) for _end in range(_start + 1, len_a)]
    if res:
	return max(res)
    else:
	return 0

def largestRectangleArea(self, height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans

def mine(arr):
    len_a = len(arr)
    s = []
    ple = [-1] * len_a
    for i in range(len_a):
        while s and arr[s[-1]] > arr[i]:
            s.pop()
        ple[i] = s[-1] if s else -1
        s.append(i)

    s = []
    nle = [len_a] * len_a
    for i in range(len_a):
        while s and arr[s[-1]] > arr[i]:
            nle[s.pop()] = i
        s.append(i)

    max_found = -sys.maxsize -1
    for i in range(len_a):
        max_found = max(max_found, arr[i] * (nle[i] - ple[i] - 1))

    return max_found


def test():
    assert mine([1, 2, 3, 4, 5]) == 9
    assert mine([5, 4, 3, 2, 1]) == 9
    assert mine([1, 2, 5, 4, 3]) == 9
    assert mine([4, 3, 1, 2, 5]) == 6
    assert mine([1, 2, 5, 3, 4]) == 9
    assert mine([5, 3, 4, 1, 2]) == 9

if __name__ == "__main__":
    test()

