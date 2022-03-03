#!/usr/bin/env python
import sys
import heapq

def dijkstra(g, s, t):
    hq = []
    dp = {k: sys.maxsize for k in g.keys()}
    p = {}

    dp[s] = 0
    heapq.heappush(hq, (0, s))

    while hq:
        last_w, curr_v = heapq.heappop(hq)
        for n, n_w in g[curr_v]:
            if last_w + n_w < dp[n]:
                dp[n] = last_w + n_w
                p[n] = curr_v
                heapq.heappush(hq, (dp[n], n))
                
    print("predecessors: " + str(p))
    print("delta: ", str(dp))
    return dp[t]


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


