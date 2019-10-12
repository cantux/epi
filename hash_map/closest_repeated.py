#!/usr/bin/env python
import sys
from collections import defaultdict

def fnc(arr):
    closest = sys.maxint
    record = dict()

    for i, el in enumerate(arr):
        if el in record:
            # record {el: (last position, distance to last)}
            curr = record[el]
            curr_distance_to_last = i - curr[0] - 1
            if curr[1] > curr_distance_to_last:
                curr[1] = curr_distance_to_last
            closest = min(curr[1], closest)
            curr[0] = i
        else:
            record[el] = [i, sys.maxsize]
    return closest

def test():
    assert fnc([]) == sys.maxint
    assert fnc(['a', 'b', 'a']) == 1
    assert fnc(['a', 'x', 'y', 'a', 'y']) == 1

if __name__ == "__main__":
    test()

