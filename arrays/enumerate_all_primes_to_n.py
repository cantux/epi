#!/usr/bin/env python

# sieve of erathosthenes

def sieve(n):
    p = 2
    bucket = [False for i in range(n)]
    while p * p <=n:
        if not bucket[p]:
            for i in range(p + p, n, p):
                bucket[i] = True
        p += 1
    res = []
    for i in range(2, n):
        if not bucket[i]:
            res.append(i)
    return res

def test():
    print(sieve(99))

if __name__ == "__main__":
    test()

