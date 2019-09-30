#!/usr/bin/env python

import heapq

def merge(files):
    aux_h = []
    heapq.heapify(aux_h)
    for i in range(len(files)):
        heapq.heappush(aux_h, (files[i][0], i, 0))
    
    f_len_map = {i: len(files[i]) for i in range(len(files))}
    
    ret = []
    while aux_h:
        val, f_idx, el_i = heapq.heappop(aux_h)
        if el_i < f_len_map[f_idx] - 1:
            heapq.heappush(aux_h, (files[f_idx][el_i + 1], f_idx, el_i + 1))
        ret.append(val)
    return ret

def test():
    files = []
    files.append(range(6)[::3])
    files.append(range(6)[1::3])
    files.append(range(6)[2::3])
    assert merge(files) == sorted(range(6))

if __name__ == "__main__":
  test()

