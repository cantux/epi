#!/usr/bin/env python

import random

def sort(arr):
    _sort(arr, 0, len(arr) - 1)

def _sort(arr, start, end):
    if start < end:
        pivot = rand_partition(arr, start, end)
                    
        _sort(arr, start, pivot - 1)
        _sort(arr, pivot + 1, end)

def rand_partition(arr, start, end):
    piv_idx = random.randint(start, end) 
    arr[piv_idx], arr[end] = arr[end], arr[piv_idx]
    return partition(arr, start, end)

def partition(arr, start, end):
    """
    move elements around a particular pivot.
    """
    pivot = arr[end]
    small_ptr = start
    big_ptr = end - 1 

    for i in range(start, end):
        if arr[i] > pivot:
            arr[i], arr[big_ptr] = arr[big_ptr], arr[i]
            big_ptr -= 1
        else:
            arr[i], arr[small_ptr] = arr[small_ptr], arr[i]
            small_ptr += 1
        
    arr[end], arr[small_ptr] = arr[small_ptr], arr[end]
    
    return small_ptr

arr = range(10)
print("parted around: {0}".format(rand_partition(arr, 0, len(arr) - 1)))
print("after part arr is: ", arr)
sort(arr)
print("arr is: ", arr)

print(sort(list(reversed(arr))))
print("arr is: ", arr)
