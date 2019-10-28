#!/usr/bin/env python

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj = defaultdict(set)

    def addVertex(self, node):
        if node not in self.adj:
            self.adj[node] = set()

    def addEdge(self, node1, node2):
        if node1 not in self.adj:
            self.addVertex(node1)
        if node2 not in self.adj:
            self.addVertex(node2)
        self.adj[node1].add(node2)

    def printAdj(self):
        print "g is: "
        for (k, v) in self.adj.items():
            print "vertex k: ", k, "has edges: ", list(v)

    def dfs(self, s):
        seen = set()
        def visit(self, v):
            print "visiting: ", v
            seen.add(v)
            for n in self.adj[v]:
                if n not in seen:
                    visit(self, n)
        visit(self, s) 

def test():
    g = Graph()
    g.addEdge("a", "b")
    g.addEdge("b", "c")
    g.addEdge("c", "d")
    g.addEdge("d", "e")
    g.addEdge("b", "e")
    g.addEdge("a", "a")
    
    g.dfs("a")

if __name__ == "__main__":
    test()

