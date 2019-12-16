#!/usr/bin/env python
import sys
def brut(tasks):
    len_t = len(tasks)
    tasks.sort(key=lambda x: x[1])
    print tasks
    def rec(curr_idx):
        if curr_idx >= len_t:
            return 0
        max_w = tasks[curr_idx][2]
        next_task = find_next(curr_idx, tasks[curr_idx][1])
        if next_task:
            max_w += rec(next_task)
        return max(max_w, rec(curr_idx + 1))

    def find_next(curr, curr_end):
        for i in range(curr + 1, len_t):
            if tasks[i][0] >= curr_end:
                return i

    return rec(0)

def tab(tasks):

def test():
    assert brut([(3, 10, 20), (1, 2, 50), (6, 19, 100), (2, 100, 200)]) == 250

if __name__ == "__main__":
    test()

