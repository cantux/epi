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
                parents.add(node)
                for n in self.adj[node]:
                    if n in parents:
                        return True
                    if n not in seen:
                        if det(n, parents):
                            return True
                parents.remove(node)
                
            return False

        for (k,v) in self.adj.items():
            if det(k, set()):
                return True
        return False

    def det_nice(g):
        graph = [[] for _ in range(numCourses)]
        indegree = [0, ] * numCourses
        for to_, from_ in prerequisites:
            graph[from_].append(to_)
            indegree[to_] += 1
            
        queue = collections.deque(v for v in range(numCourses) 
                                  if indegree[v] == 0)
        n = len(queue)
        while queue and n != numCourses: # adding n != numCourses to terminate loop earlier
            v = queue.popleft()
            for to_ in graph[v]:
                indegree[to_] -= 1
                if indegree[to_] == 0:
                    n += 1
                    queue.append(to_)
        return n == numCourses
def test():
    g = Graph()
    g.addEdge("a", "b")
    g.addEdge("b", "c")
    g.addEdge("c", "a")
    assert g.detect_cycle()

if __name__ == "__main__":
    test()

