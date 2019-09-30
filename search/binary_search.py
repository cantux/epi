#!/usr/bin/env python

def bin_search(lst, item):
    mid, start, end = 0, 0, len(lst)
    
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == item:
            return mid
        elif lst[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    return -1
def test():
    lst = range(1, 10)
    assert bin_search(lst, 1) == 0
    assert bin_search(lst, 0) == -1


if __name__ == "__main__":
  test()

