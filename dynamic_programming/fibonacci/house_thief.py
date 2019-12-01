#!/usr/bin/env python

# n houses nuilt in a line
# thief wants to steal maximum possible money from these houses
# only restriction is that he can't steal from two consecutive houses
# maximize stealing

def brut(vals):
    len_v = len(vals)
    def rec(curr_idx):
        if curr_idx >= len_v:
            return 0
        return max(rec(curr_idx + 2) + vals[curr_idx], 
                rec(curr_idx + 1))
    return rec(0)

def memo(vals):
    len_v = len(vals)
    dp = [-1 for _ in range(len_v)]
    def rec(curr_idx):
        if curr_idx >= len_v:
            return 0
        if dp[curr_idx] == -1:
            dp[curr_idx] = max(rec(curr_idx + 2) + vals[curr_idx], 
                rec(curr_idx + 1))
        return dp[curr_idx]
    return rec(0)

import sys
def tab(vals):
    len_v = len(vals)
    dp = [-sys.maxint - 1 for i in range(len_v + 1)]
    dp[0] = 0
    dp[1] = vals[0]
    for i in range(1, len_v):
        dp[i + 1] = max(dp[i], dp[i - 1] + vals[i])
    print dp
    return dp[len_v]


def opt(vals):
    n = len(wealth)
    if n == 0:
        return 0
    n1, n2 = 0, wealth[0]
    for i in range(1, n):
        n1, n2 = n2, max(n1 + wealth[i], n2)
    return n2


def test():
    assert brut([2, 5, 1, 3, 6, 2, 4]) == 15
    assert brut([2, 10, 14, 8, 1]) == 18
    assert memo([2, 5, 1, 3, 6, 2, 4]) == 15
    assert memo([2, 10, 14, 8, 1]) == 18
    assert tab([2, 5, 1, 3, 6, 2, 4]) == 15
    assert tab([2, 10, 14, 8, 1]) == 18



if __name__ == "__main__":
    test()

