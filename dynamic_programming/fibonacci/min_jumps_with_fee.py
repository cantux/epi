#!/usr/bin/env python

# given a staricase with n steps
# and an array of n numbers representing the fee that you have to pay if you take the step
# at every step you have the option to take 1, 2 or 3 steps.
# assume you are standing on the first step.
# ex: {1, 2, 5, 2, 1, 2} -> 3 -> 0-3-top

import sys

def tab(fees):
    n = len(fees)
    dp = [sys.maxint for _ in range(n + 1)]
    dp[0] = 0
    for i in range(n):
        for j in range(1, 4):
            if i + j <= n:
                dp[i + j] = min(dp[i + j], dp[i] + fees[i])

    print dp
    return dp[n]
        

def test():
    assert tab([1, 2, 5, 2, 1, 2]) == 3
    assert tab([2,3,4,5]) == 5

if __name__ == "__main__":
    test()

