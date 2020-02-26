
from djs import DisjointSet

def kruskal(edges, vertices):
    djs = DisjointSet(vertices)

    edges.sort(lambda x: x[2])

    for e in edges:
        if djs.find(e[0]) != djs.find(e[1]):
            djs.union(e[0], e[1])