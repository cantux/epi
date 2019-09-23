#!/usr/bin/env python

class TreeP:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent 
        self.left = None
        self.right = None

def succ(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    while node.parent and node.parent.right is node:
            node = node.parent
    
    return node.parent
    
def ino(tree):
    lst = []
    ino_r(tree, lst)
    return lst

def ino_r(tree, lst):
    if not tree:
        return
    ino_r(tree.left, lst)
    print tree.val
    lst.append(tree)
    ino_r(tree.right, lst)

def create_tree():
    tree = TreeP(0, None)

    tree.left = TreeP(1, tree)
    tree.right = TreeP(2, tree)
    
    tree.left.left = TreeP(3, tree.left)
    tree.left.right = TreeP(4, tree.left)

    tree.right.left = TreeP(5, tree.right)
    tree.right.right = TreeP(6, tree.right)

    tree.left.left.left = TreeP(7, tree.left.left)
    tree.left.left.right = TreeP(8, tree.left.left)

    tree.left.right.right = TreeP(9, tree.left.right)

    tree.right.right.left = TreeP(10, tree.right.right)
    return tree

def test():
    tree = create_tree()       
    t_t = ino(tree)

    t_l = []
    for i in range(len(t_t) - 1):
        t_l.append((t_t[i], t_t[i + 1]))

    for t in t_l:
        print t[0].val, t[1].val
        assert succ(t[0]) == t[1]
 
if __name__ == "__main__":
  test()

