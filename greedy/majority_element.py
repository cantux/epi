#!/usr/bin/env python

def majority_element(A):
    candidate, candidate_count = None, 0
    for a in A:
        if candidate_count == 0:
            candidate, candidate_count = a, 1
        elif candidate == a:
            candidate_count += 1
        else:
            candidate_count -= 1
    return candidate

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

