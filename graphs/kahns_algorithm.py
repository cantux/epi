#!/usr/bin/env python

from collections import defaultdict
def topo_sort(g):
    # compute indegree for each of the vertex present in the DAG 
    indegree_dct = defaultdict(int)
    
    for k in g.keys():
        indegree_dct[k] = 0

    for k in g.keys():
        for v, v_w in g[k].items():
            indegree_dct[v] += 1

    q = []
    for v, d in indegree_dct.items():
        if d == 0:
            q.append(v)

    visited_count = 0
    top_order = []
    while q:
        curr = q.pop(0)
        top_order.append(curr)

        visited_count += 1
        if curr in g:
            for v, v_w in g[curr].items():
                indegree_dct[v] -= 1
                if indegree_dct[v] == 0:
                    q.append(v)
    
    if visited_count != len(indegree_dct):
        return []
    return top_order
    # initialize the couunt of visited nodes as 0.

    return None

def test():
    dag = [("x", "s", 5), 
            ("x", "a", 3),
            ("s", "a", 2), 
            ("s", "b", 6), 
            ("a", "b", 7), 
            ("a", "c", 4), 
            ("a", "d", 2), 
            ("b", "d", 1),
            ("b", "c", -1),
            ("c", "d", -2),
            ]
 
    vew = [("s", "a", 1), 
            ("s", "b", 2), 
            ("a", "c", 5), 
            ("a", "b", 3), 
            ("b", "a", 1), 
            ("a", "e", 2), 
            ("c", "e", 3),
            ("e", "f", 4),
            ("e", "d", 1),
            ("d", "c", 2),
            ("b", "d", 1),
            ("d", "f", 1),
            ]   
    g = {}
    for d in vew:
        if d[0] not in g:
            g[d[0]] = {}
        g[d[0]].update({d[1]: d[2]})

    print topo_sort(g)

if __name__ == "__main__":
    test()

