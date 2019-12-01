#!/usr/bin/env python

import sys

def knap_tab(profits, weights, cap):
    len_w = len(weights)
    dp = [[0 for _ in xrange(cap + 1)] for _ in range(len_w)]
    
    for c in range(cap + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, len_w):
        res = 0 
        for used in range(1, cap + 1):
            if used - weights[i] >= 0:
                res = max(res, dp[i - 1][used - weights[i]] + profits[i], \
                                    dp[i - 1][used])
            else:
                res = max(res, dp[i - 1][used])
            dp[i][used] = res
    return dp[len_w - 1][cap]

def test():
    assert knap_brut([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
    assert knap_brut([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17
#     assert knap_wrong([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
#     assert knap_wrong([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17

    assert knap_tab([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
    assert knap_tab([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17

if __name__ == "__main__":
    test()

