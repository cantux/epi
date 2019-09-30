#!/usr/bin/env python

def check(tree, node):
    if not tree:
        return False
    return tree == node or check(tree.left, node) or check(tree.right, node)

class Tree:
    def __init__(self, val=None):
        self.right = None
        self.left = None
        self.val = val
def test():
    t = Tree(0)
    t.left = Tree(1)
    t.right = Tree(2)
    t.left.left = Tree(3)
    t.left.right = Tree(4)
    t.right.left = Tree(5)
    t.right.right = Tree(6)
    assert check(t, t.right)

if __name__ == "__main__":
    test()

