#!/usr/bin/env python

def brute(lengths, prices, rod_length):
    len_a = len(lengths)

    def rec(rem_length, curr_idx):
        if rem_length <= 0 or curr_idx >= len_a:
            return 0
        profit = rec(rem_length, curr_idx + 1)
        if rem_length >= lengths[curr_idx]:
            profit = max(profit, prices[curr_idx] + rec(rem_length - lengths[curr_idx], curr_idx))
        return profit
    
    return rec(rod_length, 0)

def tab(lengths, prices, rod_length):
    len_a = len(lengths)
    dp = [[0 for _ in range(rod_length + 1)] for _ in range(len_a)]

    for i in range(len_a):
        for rod_rem in range(1, rod_length + 1):
            if i >= 0:
                dp[i][rod_rem] = dp[i - 1][rod_rem]
            if lengths[i] <= rod_rem:
                dp[i][rod_rem] = max(dp[i][rod_rem], prices[i] + dp[i][rod_rem - lengths[i]])
    print dp
    return dp[len_a - 1][rod_length]

def test():
    assert brute([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5) == 14
    assert tab([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5) == 14

if __name__ == "__main__":
    test()

