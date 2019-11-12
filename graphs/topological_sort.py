#!/usr/bin/env python
from collections import namedtuple

def t_sort(g):
    ret = []
    def dfs(s):
        if s in ret:
            return
        if s in g:
            for n in g[s]:
                dfs(n[0])
        ret.append(s)
    
    dfs("a")
    return ret[::-1]

def detect_cycle(g):
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


def test():
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
            g[d[0]] = []
        g[d[0]].append((d[1], d[2]))

    print g
    print t_sort(g)
    print "cylce: ", detect_cycle(g)

if __name__ == "__main__":
    test()

