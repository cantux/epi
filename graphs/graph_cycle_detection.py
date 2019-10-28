#!/usr/bin/env python

class Graph:
    def __init__(self):
        self.adj = {}

    def addEdge(self, node1, node2):
        if node1 and node1 not in self.adj:
            self.adj[node1] = set()
        if node2 and node1 not in self.adj:
            self.adj[node2] = set()
        self.adj[node1].add(node2)

    def detect_cycle(self):
        seen = set()
        def det(node, parents):
            if node not in seen:
                seen.add(node)
                for n in self.adj[node]:
                    if n in parents:
                        return True
                    parents.add(n)
                    det(n, parents)
                    parents.remove(n)
        for (k,v) in self.adj.items():
            if det(k, set()):
                return True
        return False


def fnc():
    return None

def test():
    g = Graph()
    g.addEdge("a", "b")
    g.addEdge("b", "c")
    g.addEdge("c", "a")
    assert g.detect_cycle()
    assert fnc() == None

if __name__ == "__main__":
    test()

