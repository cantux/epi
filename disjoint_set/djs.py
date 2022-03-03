class DisjointSet:
    # with union-by-rank and path compression
    def __init__(self, lst=None):
        # if something is set to itself it is the representetive of it's set
        # if you look for an element's parent and it's not itself, it is part of parent's set
        # find() recursively traverses parents
        self.parent = {} # disjoint set main datastructure

        # rank keeps the depth of the tree
        self.rank = {}

        if lst:
            for n in lst:
                self.parent[n] = n
                self.rank[n] = 0

    # given an element find it's representetive
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # given two elements, merge their disjoint sets. If they are already in the same set, there's nothing to do.
    def union(self, s1, s2):
        r_s1, r_s2 = self.find(s1), self.find(s2)
        if r_s1 == r_s2:
            return 0
        
        # if you always choose of the root of the deeper tree as our new root, it will not grow deeper.
        if self.rank[r_s1] < self.rank[r_s2]:
            self.parent[r_s1] = r_s2
        else:
            self.parent[r_s2] = r_s1
        
        if self.rank[r_s1] == self.rank[r_s2]: # handle the case where if both trees are of the same length
            self.rank[r_s1] += 1
        return 1
     
    def __repr__(self):
        return "parent: " + str(self.parent) + "\n" + "rank: " +str(self.rank)

def test():
    djs = DisjointSet(["a", "b"])
    print djs
    assert djs.find("a") == "a"
    assert djs.find("b") == "b"
    djs.union("a", "b")
    print djs
    assert djs.find("a") == "a"
    assert djs.find("b") == "a"

    # depth trials
    djs = DisjointSet(list(range(30)))
    for i,j in zip(range(29), range(1, 30)):
        djs.union(i, j)
        print djs

if __name__ == "__main__":
    test()
