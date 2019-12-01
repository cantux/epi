#!/usr/bin/env python

# given stairs with n levels and steps 
# find number of ways to make it to the top
def brut(s, l):
    len_s = len(s) 

    def rec(rem_stairs):
        if rem_stairs == 0:
            return 1
        total = 0
        for step in s:
            if rem_stairs >= step:
                total += rec(rem_stairs - step)
        return total
    return rec(l)

def memo(s, l):
    len_s = len(s)
    dp = [-1 for _ in range(l + 1)]
    def rec(rem_stairs):
        if rem_stairs == 0:
            return 1

        if dp[rem_stairs] == -1:
            total = 0
            for step in s:
                if rem_stairs >= step:
                    total += rec(rem_stairs - step)
            dp[rem_stairs] = total
        return dp[rem_stairs]

    return rec(l)

def tab(s, l):
    len_s = len(s)
    dp = [0 for _ in range(l + 1)]
    dp[0] = 1
    for i in range(l):
        for step in s:
            if i + step <= l:
                dp[i + step] += dp[i] 

    print dp
    return dp[l]

def test():
    assert brut([1, 2, 3], 3) == 4
    assert brut([1, 2, 3], 4) == 7
    assert memo([1, 2, 3], 3) == 4
    assert memo([1, 2, 3], 4) == 7
    assert tab([1, 2, 3], 3) == 4
    assert tab([1, 2, 3], 4) == 7



if __name__ == "__main__":
    test()

