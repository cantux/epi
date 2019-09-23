
#!/usr/bin/env python

from tree import Tree

def sum_t(tree):
    if not tree:
        return 0
    lst = []
    sum_h(tree, 0, lst)
    return lst

def sum_h(tree, sums, lst):
    if not tree.right and not tree.left:
        lst.append(sums + tree.val)
        print lst
        return

    sum_h(tree.left, sums + tree.val, lst)
    sum_h(tree.right, sums + tree.val, lst)

def test():
    t = Tree(0)
    t.left = Tree(1)
    t.right = Tree(2)
    t.left.left = Tree(3)
    t.left.right = Tree(4)

    t.right.left = Tree(5)
    t.right.right = Tree(6)

    assert sum_t(t.right.right) == [6]
    assert sum_t(t.right) == [7, 8]


if __name__ == "__main__":
  test()

