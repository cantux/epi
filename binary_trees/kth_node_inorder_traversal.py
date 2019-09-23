#!/usr/bin/env python

from tree import Tree

def kth(tree, k):
    kth(tree, 1, k)

def kth(tree, curr, k):
    if curr == k:
        return smt
    if not tree:
        return curr
    n = kth(tree.left, curr + 1, k)
    return kth(tree.right, n, k)

def test():
    t = Tree(0)
    t.left = Tree(1)
    t.right = Tree(2)
    t.left.left = Tree(3)
    t.left.right = Tree(4)

    t.right.left = Tree(5)
    t.right.right = Tree(6)
    
    assert kth(tree, 3) == 3


if __name__ == "__main__":
  test()

