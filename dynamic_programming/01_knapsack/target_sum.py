
#!/usr/bin/env python

def brute(arr, target):
    len_arr = len(arr)

    def rec(curr_ptr, sum1, sum2):
        if sum2 - sum1 == target \
            and curr_ptr == len_arr:
            return 1
        elif curr_ptr == len_arr:
            return 0

        return rec(curr_ptr + 1, sum1 + arr[curr_ptr], sum2) + \
                rec(curr_ptr + 1, sum1, sum2 + arr[curr_ptr])
    
    return rec(0, 0, 0)

def memo(arr, target):
    s = sum(arr)
    len_arr = len(arr)
    dp = [[-1 for _ in range(s // 2 + 1)] for _ in range(len_arr + 1)]

    def rec(curr_ptr, sum1, sum2):
        if sum2 - sum1 == target \
            and curr_ptr == len_arr:
            return 1
        elif curr_ptr == len_arr:
            return 0
        elif sum1 > s // 2:
            return 0

        if dp[curr_ptr][sum1] == -1:
            dp[curr_ptr][sum1] = rec(curr_ptr + 1, sum1 + arr[curr_ptr], sum2) + \
                                    rec(curr_ptr + 1, sum1, sum2 + arr[curr_ptr])
        return dp[curr_ptr][sum1]
    return rec(0, 0, 0)


def tab(arr, target):
    len_arr = len(arr)
    s = sum(arr)
# see that we are asked to find number of partitions with target difference
# define p1 and p2 are results of some partition. Then,
# sum(p1) - sum(p2) = target
# sum(p1) + sum(p2) = sum(arr)
# 2 * sum(p1) = target + sum(arr)
# sum(p1) = (target + sum(arr)) // 2
# => problem is converted into find partitions that sum up to new_target
    new_target = (target + s) // 2
    dp = [[0 for _ in range(new_target + 1)] for _ in range(len_arr)]
    
    for i in range(len_arr):
        dp[i][0] = 1
    
    for i in range(len_arr):
        for t in range(1, new_target + 1):
            dp[i][t] = dp[i - 1][t]
            if t >= arr[i]:
                dp[i][t] += dp[i - 1][t - arr[i]]
#     print dp
        
    return dp[len_arr - 1][new_target]

def opt(arr, target):
    len_arr = len(arr)
    s = sum(arr)
    new_target = (s + target) // 2
    dp = [0 for _ in range(new_target + 1)]
    dp[0] = 1

    ## case for single element
    for t in range(1, new_target + 1):
        if arr[0] == t:
            dp[t] = 1

    for i in range(1, len_arr):
        for t in range(new_target, -1, -1):
            if arr[i] <= t:
                dp[t] += dp[t - arr[i]]
#     print dp
    return dp[new_target]

def test():
    assert brute([1, 1, 2, 3], 1) == 3
    assert brute([1, 2, 7, 1], 9) == 2
    assert memo([1, 1, 2, 3], 1) == 3
    assert memo([1, 2, 7, 1], 9) == 2
    assert tab([1, 1, 2, 3], 1) == 3
    assert tab([1, 2, 7, 1], 9) == 2
    assert opt([1, 1, 2, 3], 1) == 3
    assert opt([1, 2, 7, 1], 9) == 2



if __name__ == "__main__":
    test()

