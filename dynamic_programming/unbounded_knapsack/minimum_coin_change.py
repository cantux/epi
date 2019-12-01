#!/usr/bin/env python
# given infinite amount of coins with denominations array and a total money amount
# find the minimum number of coins required to make up that amount.

import sys
def brut(coins, amount):
    len_c = len(coins)
    def rec(curr_idx, rem_amount):
        if rem_amount == 0:
            return 0
        elif curr_idx >= len_c or rem_amount < 0:
            return sys.maxint

        return min(rec(curr_idx + 1, rem_amount), 1 + rec(curr_idx, rem_amount - coins[curr_idx]))

    return rec(0, amount)

def memo(coins, amount):
    len_c = len(coins)
    dp  = [[-1 for _ in range(amount + 1)] for _ in range(len_c)]
    def rec(curr_idx, rem_amount):
        if rem_amount == 0:
            return 0
        elif curr_idx >= len_c or rem_amount < 0:
            return sys.maxint
        
        if dp[curr_idx][rem_amount] == -1:
            min_if_used = sys.maxint
            if coins[curr_idx] <= rem_amount:
                min_if_used = 1 + rec(curr_idx, rem_amount - coins[curr_idx])
            return min(rec(curr_idx + 1, rem_amount), min_if_used) 

    return rec(0, amount)

def tab(coins, amount):
    len_c = len(coins)
    dp = [[sys.maxint for _ in range(amount + 1)] for _ in range(len_c)]
    
    for i in range(len_c):
        dp[i][0] = 0

    for i in range(len_c):
        for rem in range(1, amount + 1):
            min_if_used = sys.maxint
            if rem >= coins[i]:
                min_if_used = dp[i][rem - coins[i]] + 1
            prefix_min = sys.maxint
            if i >= 1:
                prefix_min = dp[i - 1][rem]
            dp[i][rem] = min(min_if_used, prefix_min)
#     print dp
    return dp[len_c - 1][amount]

def test():
    assert brut([1, 2, 3], 5) == 2
    assert brut([1, 2, 3], 6) == 2
    assert brut([1], 3) == 3
    assert brut([1, 2], 5) == 3
    assert brut([1, 4, 5], 5) == 1
    assert brut([1, 2, 3], 11) == 4
    assert brut([1,2,3], 7) == 3
    assert brut([3, 5], 7) == sys.maxint
    assert memo([1, 2, 3], 5) == 2
    assert memo([1, 2, 3], 6) == 2
    assert memo([1], 3) == 3
    assert memo([1, 2], 5) == 3
    assert memo([1, 4, 5], 5) == 1
    assert memo([1, 2, 3], 11) == 4
    assert memo([1,2,3], 7) == 3
    assert memo([3, 5], 7) == sys.maxint
    assert tab([1, 2, 3], 5) == 2
    assert tab([1, 2, 3], 6) == 2
    assert tab([1], 3) == 3
    assert tab([1, 2], 5) == 3
    assert tab([1, 4, 5], 5) == 1
    assert tab([1, 2, 3], 11) == 4
    assert tab([1,2,3], 7) == 3
    assert tab([3, 5], 7) == sys.maxint


if __name__ == "__main__":
    test()

