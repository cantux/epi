#!/usr/bin/env python

import heapq

def heapsort(lst):
    heapq.heapify(lst)
    tst = []
    while lst:
        tst.append(heapq.heappop(lst))
    print tst
    return tst

def test():
    assert heapsort(range(5)[::-1]) == range(5)

if __name__ == "__main__":
  test()

