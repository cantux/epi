#!/usr/bin/env python
import sys
def t_sort(g):
    ret = []
    def dfs(s):
        if s in ret:
            return
        if s in g:
            for n in g[s]:
                dfs(n[0])
        ret.append(s)
    
    dfs("x")
    return ret[::-1]

def is_cyclic(g):
    seen = set()
    def det(node, parents):
        if node not in seen and node in g:
            seen.add(node)
            parents.add(node)
            for n in g[node]:
                if n[0] in parents:
                    return True
                if n[0] not in seen:
                    if det(n[0], parents):
                        return True
            parents.remove(node)
            
        return False

    for (k,v) in g.items():
        if det(k, set()):
            return True
    return False

def short(g, s, t):
# keep a dict of current shortest paths
# keep relaxing neighbors with dfs

    top = t_sort(g)

    slice_point = -1
    for i, v in enumerate(top):
        if v == s:
            slice_point = i

    top = top[slice_point:]
    local_sp = {t: float('inf') for t in top}
    top.pop()
    local_sp[s] = 0

    def relax(u, v):
        local_sp[v] = min(local_sp[v], local_sp[u] + g[u][v])

    print(top)
    for u in top:
        for v in g[u].keys():
            relax(u, v)

    return local_sp[t]

def fnc():
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
    
    g = {}
    for d in dag:
        if d[0] not in g:
            g[d[0]] = {}
        g[d[0]].update({d[1]: d[2]})

    print("cycle: " +  str(detect_cycle(g)))
    print(short(g, "s", "d"))


if __name__ == "__main__":
    test()

