#!/usr/bin/env python

from tree import Tree
from collections import deque

def rec_ino(tree):
    lst = []
    return rec_ino(tree, lst)

def rec_ino(tree, lst):
    if not tree: return
    ino(tree.left)
    lst.append(tree.val)
    ino(tree.right)

def test():
    t = Tree(0)
    t.left = Tree(1)
    t.right = Tree(2)
    t.left.left = Tree(3)
    t.left.right = Tree(4)

    t.right.left = Tree(5)
    t.right.right = Tree(6)
    ino(t)

if __name__ == "__main__":
  test()

