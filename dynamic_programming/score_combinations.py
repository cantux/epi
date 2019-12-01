#!/usr/bin/env python

def combinations(score):
    dp = [0] * score
    dp[2] = 1
    dp[3] = 1
    dp[4] = 1
    dp[5] = 1
    dp[6] = 2
    dp[7] = 2
    for i in range(8, score):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 7]

    print dp
    return None

def test():
    assert combinations(12) == None

if __name__ == "__main__":
    test()

