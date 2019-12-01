#!/usr/bin/env python

def subset_sum(arr, target):
    len_arr = len(arr)
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for i in range(len(arr)):
        for t in range(target, -1, -1):
            if t - arr[i] >= 0:
                dp[t] = dp[t - arr[i]] or dp[t]
    return dp[target]

def ss(arr, target):
    len_arr = len(arr)
    def rec(rem, curr):
        if rem == 0:
            return True
        if rem < 0 or curr >= len_arr:
            return False
        if rec(rem - arr[curr], curr + 1):
            return True
        return rec(rem, curr + 1)
    return rec(target, 0)

def test():
    assert subset_sum([1, 2, 3, 7], 6) == True
    assert subset_sum([1, 2, 7, 1, 5], 10) == True
    assert subset_sum([1, 3, 4, 8], 6) == False

    assert ss([1, 2, 3, 7], 6) == True
    assert ss([1, 2, 7, 1, 5], 10) == True
    assert ss([1, 3, 4, 8], 6) == False

if __name__ == "__main__":
    test()

