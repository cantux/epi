#!/usr/bin/env python

from collections import defaultdict
import pprint
import sys

def bf_dp(g, s, t):
    # convert adj list to adj dict
    og = defaultdict(dict)
    for k, v in g.items():
        for c_v, v_w in v:
            og[k].update({c_v: v_w})

    # reverse edges
    rev_g = defaultdict(set)
    for k, v in g.items():
        for c_v, _ in v:
            rev_g[c_v].add(k)

    pprint.pprint(og)
    pprint.pprint(rev_g)

    d = {s: 0}

# d(u, v) = d(u, s) + d(s, k) + d(k, v)
# d(k, v) -> find the minimum of edge weight coming in to v.
# d(s, k) -> find the minimum edge weight coming into k.
# inorder for this to work we need graph to be acyclic.
# we can do that by constraining the size of the subproblems to number of vertices 
    def find_min(curr_v, k):
        if k == 0 and curr_v == s:
            print("hit start")
            return 0
        elif k == 0:
            print("hit cycle")
            return float('inf')
        if curr_v in d:
            print("we hit memo: " + str(d[curr_v]))
            return d[curr_v]
#         if curr_v == s: # no need for this since we init delta with s = 0
#             return 0
        curr_min = float('inf')
        for incoming in rev_g[curr_v]: # all edges to incoming neighbors
            for prev_v in incoming:
#                 print "prev v: ", prev_v
                prev_min = find_min(prev_v, k - 1) + og[prev_v][curr_v]
                curr_min = min(curr_min, prev_min)

        d[curr_v] = curr_min
        pprint.pprint(d)
        return curr_min

    return find_min(t, len(g))

def test():
    og = {}
    og["s"] = [("t", 10), ("y", 5)]
    og["t"] = [("y", 2), ("x", 1)]
    og["y"] = [("t", 3), ("x", 9), ("z", 2)]
    og["z"] = [("x", 6), ("s", 7)]
    og["x"] = [("z", 4)]

    assert bf_dp(og, "s", "x") == 9

#     assert fnc() == None

if __name__ == "__main__":
    test()

