#!/usr/bin/env python

# given a list of candidates(without duplicates) and a target number
# find all unique combinations where the candidate numbers set to target

import copy

def brut(c, t):
    len_c = len(c)
    
    pi = []
    def rec(curr_idx, rem, d):
        if rem == 0:
            pi.append(copy.deepcopy(d))
            return True
        if rem < 0 or curr_idx >= len_c:
            return False
        
        d.append(c[curr_idx])
        rec(curr_idx, rem - c[curr_idx], d)
        d.pop()
        rec(curr_idx + 1, rem, d)
            
    rec(0, t, [])
    return pi

def test():
    sol1 = [[7], [2, 2, 3]]
    assert all([res in sol1 for res in brut([2, 3, 6, 7], 7)])
    sol2 = [[2, 2, 2, 2], [2, 3, 3], [3,5]]
    assert all([res in sol2 for res in brut([2, 3, 5], 8)])

if __name__ == "__main__":
    test()


