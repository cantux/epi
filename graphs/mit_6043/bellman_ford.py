#!/usr/bin/env python

import sys

# returns all paths from source to other nodes.
def shortest_weight_path(g, source, target):
    def bellman_ford():

        d = {v: sys.maxint for v in g.keys()} # tracker
        pi = {}# predecessors
    
        d[source] = 0
        for _ in range(len(g) - 1):
            for v, neighbors in g.items():
                for n, w in neighbors:
#                     print("prev edge: " + str(d[v])) # previous edge path so far
#                     print("current_edge: " + str(d[n]))
#                     print("w: " +  str(w))
                    if d[n] > d[v] + w:
                        d[n] = d[v] + w
                        pi[n] = v # set neighbor's new predecessor to be the smallest relaxed

        # negative cycle - corolarry in proof
        for v, neighbors in g.items():
            for n, w in neighbors:
                if d[n] > d[v] + w:
                    return ({}, {})

        return d, pi

    track, predecessors = bellman_ford()
    print(track)
    print(predecessors)
    return track[target]

def test():
    og = {}
    og["s"] = [("t", 10), ("y", 5)]
    og["t"] = [("y", 2), ("x", 1)]
    og["y"] = [("t", 3), ("x", 9), ("z", 2)]
    og["z"] = [("x", 6), ("s", 7)]
    og["x"] = [("z", 4)]

    assert  shortest_weight_path(og, "s", "x") == 9

if __name__ == "__main__":
    test()

