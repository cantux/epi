#!/usr/bin/env python

def brut(arr):
    len_a = len(arr)
    def rec(curr, prev):
        if curr == len_a:
            return 0
        inc_sum = 0
        if prev == -1 or arr[curr] > arr[prev]:
            inc_sum = rec(curr + 1, curr) + arr[curr]
        not_inc_sum = rec(curr + 1, prev)
        return max(inc_sum, not_inc_sum)

    return rec(0, -1)

def memo(arr):
    len_a = len(arr)
    dp = {}
    def rec(curr, prev): 
        if curr == len_a:
            return 0
        key = str(curr) + "_" + str(prev + 1)
        if key not in dp:
            inc_sum = 0
            if prev == -1 or arr[curr] > arr[prev]:
                inc_sum = rec(curr + 1, curr) + arr[curr]
            not_inc_sum = rec(curr + 1, prev)
            dp[key] = max(inc_sum, not_inc_sum)
        return dp[key]
    return rec(0, -1)

def tab(arr):
    len_a = len(arr)
    dp = [0 for _ in range(len_a)]
    dp[0] = arr[0]
    max_found = 0
    for i in range(1, len_a):
        dp[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]
        max_found = max(max_found, dp[i])
    return dp[len_a - 1]


def test():
    assert brut([4, 1, 2, 6, 10, 1, 12]) == 32
    assert brut([-4, 10, 3, 7, 15]) == 25
    assert memo([4, 1, 2, 6, 10, 1, 12]) == 32
    assert memo([-4, 10, 3, 7, 15]) == 25
    assert tab([4, 1, 2, 6, 10, 1, 12]) == 32
    assert tab([-4, 10, 3, 7, 15]) == 25

if __name__ == "__main__":
    test()

