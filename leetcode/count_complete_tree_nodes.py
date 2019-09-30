#!/usr/bin/env python

def count(tree):
    if not tree:
        return 0

    return 1 + count(tree.left) + count(tree.right)

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
    assert count(t) == 7

if __name__ == "__main__":
  test()

