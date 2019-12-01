#!/usr/bin/env python

def brute(profits, weights, capacity):
    len_a = len(weights)

    def rec(curr_profit, rem_capa, last_item_val):
        if rem_capa < 0:
            return curr_profit - last_item_val

        prof = curr_profit
        for i, w in enumerate(weights):
            prof = max(prof, 
                        rec(curr_profit + profits[i], 
                            rem_capa - w, 
                            profits[i]
                            )
                        )

        return prof

    return rec(0, capacity, 0)

import sys
def memo(profits, weights, capacity):
    len_a = len(weights)
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len_a)]

    def rec(rem_capa, curr_idx):
        if rem_capa <= 0 or curr_idx >= len_a:
            return 0
        if dp[curr_idx][rem_capa] == -1:
            prof = -sys.maxint - 1
            if weights[curr_idx] <= rem_capa:
                prof = profits[curr_idx] + rec(rem_capa - weights[curr_idx], curr_idx)

            dp[curr_idx][rem_capa] = max(prof, rec(rem_capa, curr_idx + 1))

        return dp[curr_idx][rem_capa]
    return rec(capacity, 0)

def tab(profits, weights, capacity):
    len_a = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len_a)]

    for i in range(len_a):
        for capa in range(1, capacity + 1):
            prof = -sys.maxint - 1
            if capa >= weights[i]:
                prof = profits[i] + dp[i][capa - weights[i]]
            dp[i][capa] = max(prof, dp[i - 1][capa])
    print dp
    return dp[len_a-1][capacity]

def test():
    assert brute([15, 20, 50], [1, 2, 3], 5) == 80
    assert brute([15, 50, 60, 90], [1, 3, 4, 5], 8) == 140
    assert brute([15, 50, 60, 90], [1, 3, 4, 5], 6) == 105
    assert memo([15, 20, 50], [1, 2, 3], 5) == 80
    assert memo([15, 50, 60, 90], [1, 3, 4, 5], 8) == 140
    assert memo([15, 50, 60, 90], [1, 3, 4, 5], 6) == 105
    assert tab([15, 20, 50], [1, 2, 3], 5) == 80
    assert tab([15, 50, 60, 90], [1, 3, 4, 5], 8) == 140
    assert tab([15, 50, 60, 90], [1, 3, 4, 5], 6) == 105


if __name__ == "__main__":
    test()

