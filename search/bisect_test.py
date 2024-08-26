#!/usr/bin/env python

# keep a list in sorted order without having to sort the list after each insertion.
import bisect

def test():
    # bisect_left(lst, val, lo=0, hi=len(a))
    # if val is present in lst insertion point will be before it
    lst = list(range(10)[::2])
    print(lst)
    i = bisect.bisect_left(lst, 4)
    lst.insert(i, 3)
    print(lst)
    j = bisect.bisect_right(lst, 4)
    lst.insert(j, 5)
    print(lst)

def bisect_right_to_the_end_test():
    lst = range(10)
    idx = bisect.bisect_right(lst, 11)
    print(idx)


if __name__ == "__main__":
  test()
  bisect_right_to_the_end_test()

