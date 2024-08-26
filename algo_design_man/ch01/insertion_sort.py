#!/usr/bin/env python

# separate array into sorted and unsorted segments
# insert into sorted part by adding each element from unsorted part one by one.

def insertion_sort(s):
    for i in range(1, len(s)):
        j = i
        while j > 0 and (s[j] < s[j - 1]):
            s[j], s[j - 1] = s[j - 1], s[j]
            j = j - 1
    return s

def test():
    assert insertion_sort([7, 5, 6]) == [5, 6, 7]
    assert insertion_sort([5, 6, 7]) == [5, 6, 7]
    assert insertion_sort([7, 6, 5]) == [5, 6, 7]

if __name__ == "__main__":
    test()

