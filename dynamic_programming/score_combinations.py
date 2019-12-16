#!/usr/bin/env python

def combinations(score):
    dp = [0] * (score + 1)
    dp[0] = 1

    for i in range(score - 1):
        if i + 2 < score:
            dp[i + 2] += dp[i]
        if i + 3 < score:
            dp[i + 3] += dp[i]
        if i + 7 < score:
            dp[i + 7] += dp[i]

    print dp
    return dp[score]

def test():
    assert combinations(12) == 4

if __name__ == "__main__":
    test()

