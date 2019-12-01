#!/usr/bin/env python

def min_ss_diff(arr):
    len_arr = len(arr)
    def rec(curr_ptr, sum1, sum2):
        if curr_ptr == len_arr:
            return abs(sum1 - sum2)
        
        return min(rec(curr_ptr + 1, sum1 + arr[curr_ptr], sum2),
                    rec(curr_ptr + 1, sum1, sum2 + arr[curr_ptr]))

    return rec(0, 0, 0)

def min_ss_diff_memo(arr):
    s = sum(arr)
    len_arr = len(arr)
    dp = [[-1 for x in range(s + 1)] for _ in range(len_arr)]
    def rec(curr_ptr, sum1, sum2):
        if curr_ptr == len_arr:
            return  abs(sum1 - sum2)
        if dp[curr_ptr][sum1] == -1:
            dp[curr_ptr][sum1] = min(
                            rec(curr_ptr + 1, sum1 + arr[curr_ptr], sum2),
                            rec(curr_ptr + 1, sum1, sum2 + arr[curr_ptr])
                            )
        return dp[curr_ptr][sum1]
    
    return rec(0, 0, 0)

def min_ss_diff_tab(arr):
    s = sum(arr)
    len_arr = len(arr)
    dp = [[False for _ in range(s // 2 + 1)] for _ in range(len_arr)]

    for i in range(len_arr):
        dp[i][0] = True

    for j in range(s // 2 + 1):
        dp[0][j] = arr[0] == j

    for i in range(1, len_arr):
        for j in range(1, s // 2 + 1):
            if dp[i - 1][j]:
                dp[i][j] = True
            elif j >= arr[i]:
                dp[i][j] = dp[i - 1][j - arr[i]]
    
    sum1 = 0
    # iterate backwards over the dp chart to find the maximum sum we could find
    for i in range(s // 2, -1, -1):
        if dp[len_arr - 1][i]:
            sum1 = i
            break
    sum2 = s - sum1
    return abs(sum2 - sum1)

def test():
    assert min_ss_diff([1, 2, 3, 4]) == 0
    assert min_ss_diff([1, 2, 3, 10]) == 4
    assert min_ss_diff([]) == 0
    assert min_ss_diff([1, 50, 100]) == 49
    assert min_ss_diff_memo([1, 2, 3, 4]) == 0
    assert min_ss_diff_memo([1, 2, 3, 10]) == 4
    assert min_ss_diff_memo([1, 2, 7, 1, 5]) == 0
    assert min_ss_diff_memo([1, 50, 100]) == 49

    assert min_ss_diff_tab([1, 2, 3, 4]) == 0
    assert min_ss_diff_tab([1, 2, 3, 10]) == 4
    assert min_ss_diff_tab([1, 2, 7, 1, 5]) == 0
    assert min_ss_diff_tab([1, 50, 100]) == 49

if __name__ == "__main__":
    test()

