#!/usr/bin/env python

def brut(n):
    if n == 2: return 1
    if n < 2:
        return -1

    def rec(part):
        if part == 2:
            return 2
        if part < 2:
            return 1
        max_found = 1
        for i in range(1, part):
            max_found = max(max_found, (part - i) * i, rec(part - i) * i)
        print max_found
        return max_found

    return rec(n)

def tab(n):
    dp = [1 for _ in range(n + 1)]
    dp[1] = 1

    for i in range(1, n + 1):
        for j in range(2, i):
            dp[i] = max(dp[i], dp[j] * dp[i - j], j * (i - j)) 
    return dp[n]

def test():
    assert brut(2) == 1
    assert brut(10) == 36
    assert tab(2) == 1
    assert tab(10) == 36

if __name__ == "__main__":
    test()

