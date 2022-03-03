
#!/usr/bin/env python

def bfs(g, start, target):
    level = {}
    parent = {}
    frontier = [start]
    curr_level = 1
    while frontier:
        nxt = []
        for v in frontier:
            for n in g[v]:
                if n not in level:
                    level[n] = curr_level
                    parent[n] = v
                    nxt.append(n)
        frontier = nxt
        curr_level += 1

    res = []
    curr = target
    while curr != start:
        res.append(curr)
        curr = parent[curr]

    return [start] + list(reversed(res))

from collections import defaultdict

def test():
    def addEdge(g, fr, to):
        if to not in g[fr]:
            g[fr].add(to)
        if fr not in g[to]:
            g[to].add(fr)


    g = defaultdict(set)
    addEdge(g, "a", "z")
    addEdge(g, "a", "s")
    addEdge(g, "s", "x")
    addEdge(g, "x", "d")
    addEdge(g, "x", "c")
    addEdge(g, "c", "d")
    addEdge(g, "f", "d")
    addEdge(g, "c", "f")
    addEdge(g, "v", "f")
    addEdge(g, "c", "v")

    assert bfs(g, "a", "v") == ["a", "s", "x", "c", "v"]

if __name__ == "__main__":
    test()

