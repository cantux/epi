#!/usr/bin/env python

def two_d(arr, el):
    if not arr:
        return (0, 0)

    row_len = len(arr)
    col_len = len(arr[0])

    curr = (0, col_len - 1)

    while curr[0] < row_len or curr[1] >= -1:
        val = arr[curr[0]][curr[1]]

        if el == val:
            return curr
        elif el < val:
            curr = (curr[0], curr[1] - 1)
        else:
            curr = (curr[0] + 1, curr[1])
    return (0,0)

def test():
    test_lst = [
            [-1, 2, 4, 4, 11],
            [1, 5, 5, 9, 21],
            [3, 6, 6, 9, 22],
            [3, 6, 8, 10, 24],
            [6, 8, 9, 12, 25],
            [8, 10, 12, 13, 40]
            ]
    
    # single trick solves this! 
    # START FROM THE TOP RIGHT!!
    assert two_d(test_lst, 40) == (5, 4)
    assert two_d(test_lst, 12) in [(5, 2), (4, 3)]
    assert two_d(test_lst, 11)  == (0, 4)

if __name__ == "__main__":
  test()

