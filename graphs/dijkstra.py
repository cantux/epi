#!/usr/bin/env python
import sys
import heapq

def dijkstra(g, s, t):
    q = []
    d = {k: sys.maxint for k in g.keys()}
    p = {}

    d[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        last_w, curr_v = heapq.heappop(q)
        for n, n_w in g[curr_v]:
            cand_w = last_w + n_w # equivalent to d[curr_v] + n_w 
            print d
            if cand_w < d[n]:
                d[n] = cand_w
                p[n] = curr_v
                heapq.heappush(q, (cand_w, n))
                
    print "predecessors: ", p
    print "delta: ", d
    return d[t]


def test():
    
    og = {}
    og["s"] = [("t", 10), ("y", 5)]
    og["t"] = [("y", 2), ("x", 1)]
    og["y"] = [("t", 3), ("x", 9), ("z", 2)]
    og["z"] = [("x", 6), ("s", 7)]
    og["x"] = [("z", 4)]

    assert dijkstra(og, "s", "x") == 9


if __name__ == "__main__":
    test()


