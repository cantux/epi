#!/usr/bin/env python

#exploit the fact that our target is sum /2 and reaching it in any way or form will giver me the result...
def esspp(arr):
    sum_arr = sum(arr) 
    if sum_arr % 2 != 0: return False
    target = sum_arr // 2
    len_arr = len(arr)
    dp = {}
    def rec(rem, ptr):
        if rem == 0:
            return True
        elif ptr == len_arr or rem < 0:
            return False
        if rec(rem - arr[ptr], ptr + 1):
            return True
        return rec(rem, ptr + 1)

    return rec(target, 0)

def esspp_memo(arr):
    sum_arr = sum(arr) 
    if sum_arr % 2 != 0: 
        return False
    target = sum_arr // 2
    len_arr = len(arr)
    dp = [[-1 for _ in range(target + 1)] for _ in range(len_arr)]

    def rec(rem, ptr):
        if rem == 0:
            return 1
        elif ptr >= len_arr or rem < 0:
            return 0
        if dp[ptr][rem] != -1:
            return dp[rem][ptr]
        if rec(rem - arr[ptr], ptr + 1) == 1:
            dp[ptr][rem] = 1
            return True
        dp[ptr][rem] = rec(rem, ptr + 1)
        return dp[ptr][rem]

    
    return rec(target, 0) == 1

def esspp_tab(arr):
    len_arr = len(arr)
    total = sum(arr)
    if total % 2 == 1: return False
    target = total // 2
    dp = [False] * (target + 1)
#     for a in arr:
#         dp[a] = True
    dp[0] = True
    for num in arr:
        for i in range(1, target + 1)[::-1]:
            if i >= num:
                dp[i] |= dp[i - num]
    return dp[target]


def test():
    assert esspp([1, 2, 3, 4]) == True
    assert esspp([1, 1, 3, 4, 7]) == True
    assert esspp([2, 3, 4, 6]) == False
    assert esspp([1,5,11,5]) == True
   
    assert esspp_memo([1, 2, 3, 4]) == True
    assert esspp_memo([1, 1, 3, 4, 7]) == True
    assert esspp_memo([2, 3, 4, 6]) == False
    assert esspp_memo([1,5,11,5]) == True
  
    assert esspp_tab([1, 2, 3, 4]) == True
    assert esspp_tab([1, 1, 3, 4, 7]) == True
    assert esspp_tab([2, 3, 4, 6]) == False
    assert esspp_tab([1,5,11,5]) == True
    assert esspp_tab([2,2,3,5]) == False
    
 


if __name__ == "__main__":
    test()

