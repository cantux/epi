#!/usr/bin/env python

def optimum_assignment(task_durations):
    task_durations.sort()
    len_t = len(task_durations)
    res = []
    for i, j in zip(range(len_t), range(len_t)[::-1]):
        res.append(task_durations[i], task_durations[j])
    return max(map(sum, res))

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

