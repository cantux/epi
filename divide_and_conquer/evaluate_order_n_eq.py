#!/usr/bin/env python

def eval(coef_vec, x):
    max_order = len(coef_vec)
    res = 0
    for i in range(max_order - 1, 0, -1): # range(1, max_order)[::-1]:
        res = x * (res + coef_vec[i])
    return res + coef_vec[0]

def test():

    # 2 + 2x + 2*(x^2)
    assert eval([2, 2, 2], 1) == 6
    assert eval([2, 2, 2], 2) == 14
    assert eval([1, 2, 2], 1) == 5
    assert eval([1, 2, 2], 2) == 13


if __name__ == "__main__":
    test()

