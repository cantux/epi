#!/usr/bin/env python

import sys

def brut(lengths, N):
    len_l = len(lengths)

    def rec(curr_idx, rem):
        if rem == 0:
            return 0
        elif curr_idx >= len_l or rem < 0:
            return -sys.maxint - 1

        used_curr = -sys.maxint - 1
        if lengths[curr_idx] <= rem:
            used_curr = rec(curr_idx, rem - lengths[curr_idx]) + 1

        return max(used_curr, rec(curr_idx + 1, rem))

    return rec(0, N)

def memo(lengths, N):
    len_l = len(lengths)
    dp = [[-sys.maxint - 1 for i in range(N + 1)] for _ in range(len_l)]

    def rec(curr_idx, rem):
        if rem == 0:
            return 0
        elif curr_idx >= len_l or rem < 0:
            return -sys.maxint - 1
        if dp[curr_idx][rem] == -sys.maxint - 1:
            used_curr = -sys.maxint - 1
            if lengths[curr_idx] <= rem:
                used_curr = rec(curr_idx, rem - lengths[curr_idx]) + 1
            dp[curr_idx][rem] = max(used_curr, rec(curr_idx + 1, rem))

        return dp[curr_idx][rem]

    return rec(0, N)

def tab(lengths, N):
    len_l = len(lengths)
    dp = [[-sys.maxint - 1 for i in range(N + 1)] for _ in range(len_l)]

    for i in range(len_l):
        dp[i][0] = 0
    for i in range(len_l):
        for rem in range(1, N + 1):
            prefix_max = -sys.maxint - 1
            if i > 0:
                prefix_max = dp[i - 1][rem]
            used_max = -sys.maxint - 1
            if rem >= lengths[i]:
                used_max = dp[i][rem - lengths[i]] + 1
            dp[i][rem] = max(prefix_max, used_max)
    return dp[len_l - 1][N]

def test():
    assert brut([2, 3, 5], 5) == 2
    assert brut([3, 2, 5], 5) == 2
    assert brut([2, 5], 5) == 1
    assert brut([3], 5) == -sys.maxint
    assert brut([2, 3], 7) == 3
    assert memo([2, 3, 5], 5) == 2
    assert memo([3, 2, 5], 5) == 2
    assert memo([2, 5], 5) == 1
    assert memo([3], 5) == -sys.maxint
    assert memo([2, 3], 7) == 3
    assert tab([2, 3, 5], 5) == 2
    assert tab([3, 2, 5], 5) == 2
    assert tab([2, 5], 5) == 1
    assert tab([3], 5) == -sys.maxint
    assert tab([2, 3], 7) == 3

if __name__ == "__main__":
    test()

