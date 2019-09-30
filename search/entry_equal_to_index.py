#!/usr/bin/env python

def find_equal_index(lst):
    lo, hi = 0, len(lst)

    while lo < hi:
        mid = (lo + hi) //2
        if lst[mid] == mid:
            return mid
        elif lst[mid] < mid:
            lo = mid + 1
        else:
            hi = mid - 1
def test():
  assert 1 == 1

if __name__ == "__main__":
  test()

