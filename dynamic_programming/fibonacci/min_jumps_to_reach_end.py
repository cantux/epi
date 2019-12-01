#!/usr/bin/env python

# given an array of jumps where each element represent 
# how far it can jump
# find the minimum number of jumps required.
def brut(jumps):
    return None

import sys
def tab(jumps):
    len_jumps = len(jumps)
    dp = [sys.maxint for _ in range(len_jumps)]
    dp[0] = 0
    for i in range(len_jumps):
        for j in range(1, jumps[i] + 1):
            if i + j < len_jumps:
                dp[i + j] = min(dp[i + j], dp[i] + 1)

    print dp
    return dp[len_jumps - 1]

def test():
    assert tab([2, 1, 1, 1, 4]) == 3
    assert tab([1, 1, 3, 6, 9, 3, 0, 1, 3]) == 4

if __name__ == "__main__":
    test()

