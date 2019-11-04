#!/usr/bin/env python

class Graph:
    def __init__(self):
        self.vertices = {}
    def addEdge(self, node1, node2):
        if node1 not in vertices:
            vertices[node1] = set()
        if node2 not in vertices:
            vertices[node2] = set()
        vertices[node1].add(node2)

def fnc():
    return None

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

