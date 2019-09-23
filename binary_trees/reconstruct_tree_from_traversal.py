#!/usr/bin/env python

# many trees can exists from given a single preorder, inorder or postorder traversal.
# How ever there is only one tree that can be constructed from a given inorder traversal and one other.

# given preorder and inorder traversal of a tree, reconstruct the tree

from successor import create_tree, ino_r



def cons(preorder, inorder):
    pass

def preo(tree, lst):
    if not tree:
        return
    lst.append(tree)
    preo(tree.left, lst)
    preo(tree.right, lst)

def test():
    t = create_tree()
    preorder = preo(t)
    inorder = ino_r(t)
    assert cons(preorder, inorder) == t

if __name__ == "__main__":
    test()

