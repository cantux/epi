#!/usr/bin/env python

def fnc(A, B):
    return all([a > b for a, b in zip(sorted(A), sorted(B))])

def test():
    assert fnc([4, 5, 6], [1, 2 ,3])

if __name__ == "__main__":
    test()

