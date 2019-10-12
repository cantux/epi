#!/usr/bin/env python

import random

def part_around_el(lst, piv_idx, piv_start, piv_end):
    if piv_start >= piv_end:
        return piv_idx

    pivot = lst[piv_idx]
    lst[piv_idx], lst[piv_end] = lst[piv_end], lst[piv_idx]

    small_ptr = piv_start
    big_ptr = piv_end - 1 
    while small_ptr < big_ptr:
        if lst[small_ptr] > pivot:
            lst[small_ptr], lst[big_ptr] = lst[big_ptr], lst[small_ptr]
            big_ptr -= 1
        else:
            small_ptr += 1

    if lst[small_ptr] < pivot:
        small_ptr += 1
            
    lst[piv_end], lst[small_ptr] = lst[small_ptr], lst[piv_end]
    return small_ptr

def shuffle(lst):
    i = 0
    for i in range(len(lst)):
        pos = random.randint(i, len(lst) - 1)
        lst[i], lst[pos] = lst[pos], lst[i] 

def test():
    part_test = range(100)
    for i in range(100):
        shuffle(part_test)
        idx = part_around_el(part_test, i, 0, len(part_test) - 1)
        # verify correctness of part
        for i in range(0, idx):
            assert part_test[i] < part_test[idx]
        for j in range(idx + 1, len(part_test)):
            assert part_test[j] > part_test[idx]

if __name__ == "__main__":
  test()

