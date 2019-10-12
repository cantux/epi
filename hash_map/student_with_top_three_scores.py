#!/usr/bin/env python

import sys
import heapq

def fnc(scores):
    m = {}
    known_max = -sys.maxsize - 1
    found_student = ""
    for (n,s) in scores:
        if n not in m:
            m[n] = {"h": [], "curr_sum": 0}
        
        if len(m[n]["h"]) == 3 and s >= m[n]["h"][0]:
            m[n]["curr_sum"] -= heapq.heappop(m[n]["h"])
            heapq.heappush(m[n]["h"], s)
            m[n]["curr_sum"] += s
        else:
            heapq.heappush(m[n]["h"], s)
            m[n]["curr_sum"] += s
        
        if m[n]["curr_sum"] > known_max and len(m[n]["h"]) == 3:
            found_student = n
            known_max = m[n]["curr_sum"]

    return (found_student, known_max)

def test():
    l = [
            ("A", 50),
            ("B", 40),
            ("C", 60),
            ("A", 50),
            ("B", 40),
            ("D", 100),
            ("D", 100),
            ("A", 50),
            ("A", 50),
            ("B", 40),
            ("C", 60),
            ("C", 60),
            ]
    assert fnc(l) == ("C", 180)

if __name__ == "__main__":
    test()

