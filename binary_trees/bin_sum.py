
#!/usr/bin/env python

from tree import Tree

def sum_bin(tree):
    if not tree:
        return 0
    return sum_bin_h(tree, 0, 0)
    
def sum_bin_h(tree, level, sm):
    if not tree:
        return 0
    new_sum = sm + (tree.val ** level)
    if not tree.right and not tree.left:
        print new_sum
        return new_sum
    return sum_bin_h(tree.right, level + 1, new_sum) + sum_bin_h(tree.left, level + 1, new_sum)
    
def test():
    t = Tree(0)
    t.left = Tree(0)
    t.right = Tree(1)

    t.left.left = Tree(0)
    t.left.right = Tree(1)
    t.right.left = Tree(0)
    t.right.right = Tree(1)
    assert sum_bin(t.right.right) == 1
    assert sum_bin(t.right.left) == 0
    assert sum_bin(t.right) == 5
    
if __name__ == "__main__":
  test()

