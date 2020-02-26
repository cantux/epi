#!/usr/bin/env python

import sys

def brut(arr):
    len_a = len(arr)
    res = []
    for window_size in range(len_a):
        max_found = -sys.maxsize - 1
        for start_index in range(len_a - window_size):
            curr = arr[start_index: window_size + start_index + 1]
            max_found = max(max_found, min(curr))
        res.append(max_found)
    return res

def stack(arr):
    len_a = len(arr)

    ple = [-1] * len_a # previous_less_element
    s = []
    for i in range(len_a):
        while s and arr[s[-1]] > arr[i]:
            s.pop()
        ple[i] = s[-1] if s else -1
        s.append(i)

    nle = [len_a] * len_a # next_less_element
    s = []
    for i in range(len_a):
        while s and arr[s[-1]] > arr[i]:
            nle[s.pop()] = i
        s.append(i)

    res = [0] * (len_a + 1)
    for i in range(len_a):
        curr_window = nle[i]-ple[i] - 1;
        res[curr_window]= max(res[curr_window], arr[i]);

    for i in range(1, len_a)[::-1]:
        res[i] = max(res[i], res[i + 1])

    return res[1:]

def test():
    assert brut([6, 3, 5, 1, 12]) == [12, 3, 3, 1, 1]

if __name__ == "__main__":
    test()

