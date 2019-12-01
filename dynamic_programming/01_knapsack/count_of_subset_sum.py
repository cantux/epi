#!/usr/bin/env python

def no_of_ss_rec(arr, target):
    len_arr = len(arr)

    def rec(curr_ptr, target):
        if target == 0:
            return 1
        elif target < 0 or curr_ptr >= len_arr:
            return 0

        return rec(curr_ptr + 1, target - arr[curr_ptr]) + rec(curr_ptr + 1, target) 

    return rec(0, target)

def no_of_ss_memo(arr, target):
    len_arr = len(arr)

    dp = [[-1 for _ in range(target + 1)] for _ in range(len_arr)] 
    def rec(curr_ptr, target):
        if target == 0:
            return 1
        elif target < 0 or curr_ptr >= len_arr:
            return 0
        if dp[curr_ptr][target] == -1:
            dp[curr_ptr][target] = rec(curr_ptr + 1, target - arr[curr_ptr]) + rec(curr_ptr + 1, target)
        return dp[curr_ptr][target]
    return rec(0, target)

def no_of_ss_tab(arr, target):
    len_arr = len(arr)
    dp = [[-1 for _ in range(target + 1)] for _ in range(len_arr)]

    for i in range(len_arr):
        dp[i][0] = 1

    for s in range(1, target + 1):
        dp[0][s] = 1 if arr[0] == s else 0

    # imagine we have a subsolution to the problem,
    for i in range(1, len_arr):
        for t in range(1, target + 1):
            dp[i][t] = dp[i - 1][t]
            if arr[i] <= t:
                dp[i][t] += dp[i - 1][t - arr[i]]

#     print dp
    return dp[len_arr - 1][target]

def no_of_ss_opt(arr, target):
    len_arr = len(arr)
    dp = [0 for x in range(target + 1)]
    dp[0] = 1
#     for s in range(1, target + 1):
#         dp[s] = 1 if arr[0] == s else 0

    for i in range(len_arr): #1, len_arr
        for s in range(target, -1, -1):
            print "i: ", i, ", arr[i]: ", arr[i], ", s: ", s
            if s>= arr[i]: 
                dp[s] += dp[s - arr[i]]
            print dp

    return dp[target]

def test():
    assert no_of_ss_rec([1, 2, 7, 1, 5], 9) == 3
    assert no_of_ss_rec([1, 1, 2, 3], 4) == 3
    assert no_of_ss_rec([1,1,1], 1) == 3
    assert no_of_ss_memo([1, 2, 7, 1, 5], 9) == 3
    assert no_of_ss_memo([1, 1, 2, 3], 4) == 3
    assert no_of_ss_memo([1,1,1], 1) == 3
    assert no_of_ss_tab([1, 2, 7, 1, 5], 9) == 3
    assert no_of_ss_tab([1, 1, 2, 3], 4) == 3
    assert no_of_ss_tab([1,1,1], 1) == 3
    assert no_of_ss_opt([1, 2, 7, 1, 5], 9) == 3
    assert no_of_ss_opt([1, 1, 2, 3], 4) == 3
    assert no_of_ss_opt([1,1,1], 1) == 3
    assert no_of_ss_opt([1,1,1], 3) == 1




if __name__ == "__main__":
    test()

