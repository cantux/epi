#!/usr/bin/env python

def search_shifted(lst, ii):
    # pivot index: pi
    # item index: ii

    # a 
    # -1- pi -2- ii -3- 
    ## if mid is at 1, ii is smaller but it's not really.
    ## if mid is at 2, ii is larger which is business as usual
    ## if mid is at 3, ii is smaller again business as usual

    # b
    # -1- ii -2- pi -3-
    ## if mid is at 1 ii is larger, business as usual
    ## if mid is at 2 ii is lower business as usual
    ## if mid is at 3 ii is larger but its not really

    # how to recover if we are at a stage where mid landed on one of these situations?
    lo, hi = 0, len(lst) - 1 
    while lo <= hi:
        mid = (lo + hi) // 2
        if ii == lst[mid]:
            return mid
        elif ii < lst[mid]:
            if lst[lo] > ii:
                lo = mid + 1
            else:
                hi = mid - 1
        elif ii > lst[mid]:
            if lst[hi] < ii:
                hi = mid - 1
            else:
                lo = mid + 1
    return -1

def test():
    lst1 = [3, 4, 5, 1, 2]
    lst2 = [4, 5, 1, 2, 3]
    assert search_shifted(lst1, 2) == 4
    assert search_shifted(lst2, 3) == 4
    assert search_shifted(lst1, 3) == 0
    assert search_shifted(lst2, 4) == 0

if __name__ == "__main__":
  test()

