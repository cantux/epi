#!/usr/bin/env python
from collections import Counter

def fnc(arr):
    size = len(arr)
    ctr = Counter(arr)
    idx_ctr = {}

    arr_ptr = 0
    for el, count in ctr.items():
        for i in range(count):
            arr[i + arr_ptr] = el
        arr_ptr += count            

def test():
    arr = [2, 1, 2, 3, 4, 3, 4, 2, 1]
    fnc(arr)
    print arr

if __name__ == "__main__":
    test()

