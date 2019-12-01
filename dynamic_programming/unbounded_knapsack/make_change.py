#!/usr/bin/env python

# number of distinct ways to make up a total amount

def brute(coins, N):
    len_c = len(coins)

    def rec(rem, curr_idx):
        if rem == 0:
            return 1
        elif curr_idx >= len_c:
            return 0

        no_of_coins = rec(rem, curr_idx + 1)
        if rem >= coins[curr_idx]:
            no_of_coins += rec(rem - coins[curr_idx], curr_idx)

        return no_of_coins
        
    return rec(N, 0)

def memo(coins, N):
    len_c = len(coins)
    dp = [[-1 for _ in range(N + 1)] for _ in range(len_c)]
    def rec(rem, curr_idx):
        if rem == 0:
            return 1
        elif curr_idx >= len_c:
            return 0
        if dp[curr_idx][rem] == -1:
            no_of_coins = rec(rem, curr_idx + 1)
            if rem >= coins[curr_idx]:
                no_of_coins += rec(rem - coins[curr_idx], curr_idx)
            dp[curr_idx][rem] = no_of_coins
        
        return dp[curr_idx][rem]
        
    return rec(N, 0)

def tab(coins, N):
    len_c = len(coins)
    dp = [[0 for _ in range(N + 1)] for _ in range(len_c)]
    for i in range(len_c):
        dp[i][0] = 1
    for i in range(len_c):
        for rem in range(1, N + 1):
            dp[i][rem] = dp[i - 1][rem]
            if rem >= coins[i]:
                dp[i][rem] += dp[i][rem - coins[i]]

    print dp
    return dp[len_c - 1][N]

def test():
    assert brute([1, 2, 3], 5) == 5
    assert brute([10, 7, 2], 14) == 3
    assert brute(list(reversed([10, 7, 2])), 14) == 3
    assert memo([1, 2, 3], 5) == 5
    assert memo([10, 7, 2], 14) == 3
    assert memo(list(reversed([10, 7, 2])), 14) == 3
    assert tab([1, 2, 3], 5) == 5
    assert tab([10, 7, 2], 14) == 3
    assert tab(list(reversed([10, 7, 2])), 14) == 3


#     assert m_c_memoized(list(reversed([10, 7, 7, 2, 2])), 14) == 2
#     assert m_c_memoized([10, 7, 7, 2, 2], 14) == 2
    
    

if __name__ == "__main__":
    test()

