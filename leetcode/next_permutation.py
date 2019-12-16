#!/usr/bin/env python

def next_perm(arr):
    len_a = len(arr)
    
    i = len_a - 1 # first non increasing suffix
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    if i == 0:
        return arr[::-1]

    # find successor pivot
    j = len_a - 1
    while arr[j] <= arr[i -  1]:
        j -= 1

    # swapem
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # reversem'
    arr[i:] = arr[len_a - 1: i - 1:-1]
    return arr

def test():
    assert next_perm([4, 5, 6]) == [4, 6, 5]
    assert next_perm([5, 6, 4]) == [6, 4, 5]
    assert next_perm([6, 5, 4]) == [4, 5, 6]



if __name__ == "__main__":
    test()

