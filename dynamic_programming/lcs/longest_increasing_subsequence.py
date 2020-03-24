
#!/usr/bin/env python

# Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). 
# In an increasing subsequence, all the elements are in increasing order (from lowest to highest).

import sys
def brut(arr):
    len_a = len(arr)
    def rec(curr, prev):
        if curr == len_a:
            return 0
        if prev == -1 or arr[curr] > arr[prev]:
            return max(rec(curr + 1, curr) + 1, rec(curr + 1, prev))
        else:
            return rec(curr + 1, prev)

    return rec(0, -1)

def brut2(arr):
    len_a = len(arr)
    def rec(curr, prev):
        if curr == len_a:
            return 0
        inc_res = 0
        if prev == -1 or arr[curr] > arr[prev]:
            inc_res = rec(curr + 1, curr) + 1
        not_inc_res = rec(curr + 1, prev)

        return max(inc_res, not_inc_res)

    return rec(0, -1)

def memo(arr):
    len_a = len(arr)
    dp = {}
    def rec(curr, prev):
        if curr == len_a:
            return 0
        key = str(curr) + "_" + str(prev + 1)
        if key not in dp:
            inc_res = 0
            if prev == -1 or arr[curr] > arr[prev]:
                inc_res = rec(curr + 1, curr) + 1
            not_inc_res = rec(curr + 1, prev)
            dp[key] = max(inc_res, not_inc_res)
        return dp[key]
    return rec(0, -1)

def tab(arr):
  len_a = len(arr)
  dp = [0 for _ in range(len_a)]
  dp[0] = 1

  max_found = 1
  for i in range(1, len_a):
    dp[i] = 1
    for j in range(i):
      if arr[i] > arr[j] and dp[i] <= dp[j]:
        dp[i] = dp[j] + 1
        max_found = max(max_found, dp[i])

  return max_found

def test():
    assert brut([4,2,3,6,10,1,12]) == 5 
    assert brut2([4,2,3,6,10,1,12]) == 5
    assert memo([4,2,3,6,10,1,12]) == 5
    assert tab([4,2,3,6,10,1,12]) == 5

if __name__ == "__main__":
    test()

