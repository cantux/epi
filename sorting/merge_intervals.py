#!/usr/bin/env python

def fnc(intervals):
    intervals.sort(key=lambda x: x[0])
    ret_lst = []

    finish = 0
    prev_start = 0
    for inter in intervals:
        if inter[0] <= finish:
            if inter[1] > finish:
                finish = inter[1]
            pass
        else:
            ret_lst.append((prev_start, finish))
            prev_start = inter[0]
            finish = inter[1]
    ret_lst.append((prev_start, finish))
    return ret_lst

def test():
    intervals = [
            (0, 5),
            (1, 3),
            (6, 8),
            (7, 9),
            (8, 12)
            ]
    assert fnc(intervals) == [(0,5), (6, 12)]

if __name__ == "__main__":
    test()

