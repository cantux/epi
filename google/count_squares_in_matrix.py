#!/usr/bin/env python

def fnc(matrix):
    if not matrix:
        return 0

    len_r = len(matrix)
    len_c = len(matrix[0])

    res = 0
    for r in range(1, len_r):
        for c in range(1, len_c):
            if matrix[r][c] != 0:
                matrix[r][c] = min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r][c - 1]) + 1
                res += matrix[r][c]

    for r in range(len_r):
        res += matrix[r][0]

    for c in range(1, len_c):
        res += matrix[0][c]

    return res

def test():
    assert fnc([[0,1,1,1],[1,1,1,1],[0,1,1,1]]) == 15
    assert fnc([[1,0,1],[1,1,0],[1,1,0]]) == 7

if __name__ == "__main__":
    test()

