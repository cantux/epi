#!/usr/bin/env python

#decomp
## given an array a b c d e find the length of the substring that does not include repeating characters
## explanation is straight forward enough
### brute force solution
### look into n^2 subsets 1-2, 1-3, 1-4 ... 1-n, f, f + 1, ... n^2 
### and go through all thelements while keeping track of the longest
# we should be able to do better with a sliding window sort of algorithm
# 

import sys

def fnc(s):
    len_s = len(s)
    left, right = 0, 0
    freq_map = [0] * 26
    found = -sys.maxsize - 1
    while right < len_s: 
        curr = ord(s[right]) - 97 
        freq_map[curr] += 1
        if freq_map[curr] < 2:
            found = max(found, right - left + 1)
        else:
            while freq_map[curr] != 1:
                freq_map[left] -= 1
                left += 1
        right += 1
    if found == -sys.maxsize - 1:
        return 0
    if found == 0:
        return 1
    else: return found

def test():
    assert fnc('') == 0
    assert fnc('a') == 1
    assert fnc('ab') == 2
    assert fnc('abc') == 3
    assert fnc('abca') == 3
    assert fnc('abcb') == 3
    assert fnc('abac') == 3

if __name__ == "__main__":
    test()

