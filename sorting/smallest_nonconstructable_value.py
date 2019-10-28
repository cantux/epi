#!/usr/bin/env python
# decomp
# smallest value change that can't be made
# tactic, try with small values to see that sum of the previous values
# to see that if the next element is larger than the previous sum + 1
# answer is previous sum + 1

def fnc(lst):
    lst.sort()
    res = lst[0]
    for i in range(1, len(lst)):
        if res + 1 < lst[i]
            return res + 1
        res += lst[i]

    return res + 1

def test():
    lst = range(1, 4)[::-1]
    assert fnc(lst) == None

if __name__ == "__main__":
    test()

