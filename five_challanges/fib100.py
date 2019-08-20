from collections import defaultdict

def fib1(num):
    if num <= 0:
        return 0
    if num == 1:
        return 1
    return fib(num - 2) + fib(num - 1) 

mem = defaultdict() 

def fib2(num):
    if num <= 0:
        return 0
    if num == 1:
        return 1
    if num - 2 in mem:
        return fib(num - 1) + mem[num -2]
    mem[num] = fib(num - 1) + fib(num -2)
    return mem[num]

def fib(num):
    cur1 = 0
    cur2 = 1
    i = 0
    while i < num:
        temp = cur1
        cur1 = cur1 + cur2
        cur2 = temp
        i += 1
    return cur1

import time

def test():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    granularity = 100
    rec_avg, boup_avg = 0, 0
    for _ in xrange(granularity):
        rec_start = time.time()
        fib2(100)
        rec_end = time.time()
        rec_avg += (rec_end - rec_start) / granularity
        boup_start = time.time()
        fib(100)
        boup_end = time.time()
        boup_avg += (boup_end - boup_start) / granularity
    print "boup_avg: {0}, rec_avg: {1}".format(boup_avg, rec_avg)

if __name__ == "__main__":
    test()
