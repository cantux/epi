#!/usr/bin/env python

from tree import Tree

def find_sum(tree, sub):
    if not tree: return False
    if not tree.left and not tree.right and sub == tree.val:
        return True
    part_sub = sub - tree.val
    return find_sum(tree.left, part_sub) or find_sum(tree.right, part_sub)
    
def test():
    t = Tree(0)
    t.left = Tree(1)
    t.right = Tree(2)
    t.left.left = Tree(3)
    t.left.right = Tree(4)

    t.right.left = Tree(5)
    t.right.right = Tree(6)
    
    assert not find_sum(t.right.left, 6)
    assert find_sum(t.right.left, 5)

    assert not find_sum(t.right, 0)
    assert not find_sum(t.right, 5)
    assert not find_sum(t.right, 6)

    assert find_sum(t.right, 7)
    assert find_sum(t.right, 8)

if __name__ == "__main__":
  test()

