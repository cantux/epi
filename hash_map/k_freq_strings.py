#!/usr/bin/env python

from collections import Counter
import heapq

def fnc(s, k):
    if not k or not s: return []
    
    s_freq_map = Counter(s)
    
    res = []
    for text, freq in s_freq_map.items():
        if len(res) == k and res[0][1] < freq:
            heapq.heappop(res)
            heapq.heappush(res, (text, freq))
        else:
            heapq.heappush(res, (text, freq))
    return [text for text, freq in res]

def check_helper(expected, given):
    return all(map(lambda single_given: single_given in expected, given))

def test():
    assert check_helper(["a"], ["a"])
    assert check_helper([],[])
    assert check_helper(["a", "b"], ["b", "a"])
    assert fnc([], 0) == []
    assert fnc(["a", "b"], 0) == []
    assert check_helper(fnc(["a", "a", "b"], 1), ["a"])
    assert check_helper(fnc(["a", "b"], 2), ["b", "a"])
    assert check_helper(fnc(["a", "b", "c", "c"], 2), ["c", "b"]) or check_helper(fnc(["a", "b", "c", "c"], 2), ["c", "a"])

if __name__ == "__main__":
    test()

