#!/usr/bin/env python

# many trees can exists from given a single preorder, inorder or postorder traversal.
# How ever there is only one tree that can be constructed from a given inorder traversal and one other.

# given preorder and inorder traversal of a tree, reconstruct the tree

from tree import Tree

def cons(preorder, inorder):
    ino_idx_map = {el: i for i, el in enumerate(inorder)}
    tree = Tree(None)
    cons_h(preorder, 0, inorder, ino_idx_map, tree.right)
    return tree.right

def cons_h(preorder, preorder_idx, inorder_half, ino_idx_map, tree):
    if not inorder_half:
        return

    curr_el = preorder[preorder_idx] 
    tree = Tree(curr_el)
    print "current preorder element: ", curr_el
    if curr_el in inorder_half:
        print "found current el"
        ino_idx = ino_idx_map[curr_el]
        print "curr el idx: ", ino_idx
        cons_h(preorder, preorder_idx + 1, inorder_half[:ino_idx], ino_idx_map, tree.right)
        cons_h(preorder, preorder_idx + 1, inorder_half[ino_idx:], ino_idx_map, tree.left) 

def ino_r(tree, lst):
    if not tree:
        return
    ino_r(tree.left, lst)
    lst.append(tree.val)
    ino_r(tree.right, lst)

def create_tree():
    tree = Tree(0)

    tree.left = Tree(1)
    tree.right = Tree(2)
    
    tree.left.left = Tree(3)
    tree.left.right = Tree(4)

    tree.right.left = Tree(5)
    tree.right.right = Tree(6)

    tree.left.left.left = Tree(7)
    tree.left.left.right = Tree(8)

    tree.left.right.right = Tree(9)

    tree.right.right.left = Tree(10)
    return tree

def preo(tree, lst):
    if not tree:
        return
    lst.append(tree.val)
    preo(tree.left, lst)
    preo(tree.right, lst)

def test():
    t = create_tree()
    preorder = []
    preo(t, preorder)
    inorder = []
    ino_r(t, inorder)
    print "preorder: ", preorder
    print "inorder: ", inorder
    assert cons(preorder, inorder) == t

if __name__ == "__main__":
    test()

