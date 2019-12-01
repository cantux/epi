#!/usr/bin/env python

def brut(s, l):
    def rec(rem):
        if rem == 0:
            return 1
        total = 0
        for i in range(1, s + 1):
            if rem - i >= 0:
                total += rec(rem - i)
        return total

    return rec(l)

def tab(s, l):
    dp = [0 for _ in range(l + 1)]
    dp[0] = 1
    for i in range(l):
        for step in range(1, s + 1):
            if i + step <= l:
                dp[i + step] += dp[i] 

#     print dp
    return dp[l]

from collections import deque
def opt(s, l):
    dp = deque([0 for _ in range(s + 1)])
    dp[0] = 1
    for i in range(l):
        for step in range(1, s + 1):
            if i + step <= l:
                dp[step] += dp[0] 
        dp.popleft()
        dp.append(0)
        print dp
#     print dp
    return dp[0]

def test():
    assert brut(3, 3) == 4
    assert brut(3, 4) == 7
    assert tab(3, 3) == 4
    assert tab(3, 4) == 7
    assert opt(3, 3) == 4
    assert opt(3, 4) == 7



if __name__ == "__main__":
    test()

