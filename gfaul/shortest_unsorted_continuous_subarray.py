#!/usr/bin/env python

# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
# You need to find the shortest such subarray and output its length.

def n_2(arr):
    len_a = len(arr)
    start = len_a
    end = 0
    for i in range(len_a - 1):
        for j in range(i + 1, len_a):
            if arr[j] < arr[i]:
                start = min(start, i)
                end = max(end, j)
    return 0 if end - start < 0 else end - start  + 1

def n_logn(arr):
    narr = sorted(arr)
    len_a = len(arr)
    start = len_a
    end = -1
    for i in range(len_a):
        if narr[i] != arr[i]:
            start = min(start, i)
            end = max(end, i)
    return end - start + 1 if end - start >= 0 else 0

def n(arr):
    len_a = len(arr)
    start = len_a
    end = 0

    s = []
    for i in range(len_a):
        while s and s[-1] > arr[i]:
            start = min(start, s.pop())
        s.append(i)

    s = []
    for i in range(len_a, -1, -1):
        while s and s < arr[i]:
            end = min(start, s.pop())
        s.append(i)
    return end - start if end - start >= 0 else 0



def test():
    assert n_2([2,6,4,8,10,9,15]) == 5
    assert n_2([1, 3, 2, 4]) == 2
    assert n_2([1,2,3,4]) == 0
    assert n_2([2,3,3,2,4]) == 3

    assert n_logn([2,6,4,8,10,9,15]) == 5
    assert n_logn([1, 3, 2, 4]) == 2
    assert n_logn([1,2,3,4]) == 0
    assert n_logn([2,3,3,2,4]) == 3

    assert n_logn([2,6,4,8,10,9,15]) == 5
    assert n_logn([1, 3, 2, 4]) == 2
    assert n_logn([1,2,3,4]) == 0
    assert n_logn([2,3,3,2,4]) == 3

if __name__ == "__main__":
    test()


