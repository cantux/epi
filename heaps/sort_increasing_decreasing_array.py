#!/usr/bin/env python

# take in the advatage of merging two sorted arrays.
def sort_almost(lst):
    # given the list see if the one before is asc or dsc
    # put the one before into one of the heaps.
    # then just merge the both
    inc, dec = [], []
    for i in range(1, len(lst)):
        prev = lst[i - 1]
        cur = lst[i]
        if prev < cur: # should I act on prev or cur.
# I don't know the trend when I begin. So I can create a special case for it.
    

    return []

def test():
    assert sort_almost(None) == []

if __name__ == "__main__":
  test()

