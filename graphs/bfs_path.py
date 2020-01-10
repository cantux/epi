#!/usr/bin/env python

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj = {}

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

    def bfs(self, start, find):
        q = deque([])
        q.append(start)
        seen = set()
        while q:
            curr = q.popleft()
            if curr == find:
                return True
            if curr not in seen:
                seen.add(curr)
                map(lambda x: q.append(x), self.adj[curr])
        return False
    
    def shortest(self, start, end):
        """
        keep all the paths from start to the end's level
        """
        q = deque([])
        q.append(start)
        parents = {start: None}
        seen = set()
        while q:
            curr = q.popleft()
            if curr == end:
                break
            if curr not in seen:
                seen.add(curr)
                for n in self.adj[curr]:
                    parents[n] = curr
                    q.append(n)

        def traverseParentsBw(curr, s, path_stack):
            if curr == s:
                path_stack.appendleft(curr)
                return path_stack
            path_stack.appendleft(curr)
            return traverseParentsBw(parents[curr], s, path_stack)
        path_stack = deque([])
        return traverseParentsBw(end, start, path_stack)

def test():
    g = Graph()
    g.addVertex("a")
    g.printAdj()
    g.addEdge("a", "b")
    g.printAdj()
    g.addVertex("c")
    g.printAdj()
    assert g.bfs("a", "b")
    assert not g.bfs("a", "c")
    g.addEdge("b", "c")
    g.printAdj()
    assert g.bfs("a", "c")
    print g.shortest("a", "c")
    print g.shortest("b", "c")

    g.addEdge("a", "c")
    g.printAdj()
    assert g.bfs("a", "c")
    print g.shortest("a", "c")

if __name__ == "__main__":
    test()

