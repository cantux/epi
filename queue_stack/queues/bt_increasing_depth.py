
#!/usr/bin/env python

from collections import deque

class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def bt_level(bt):
    q = deque([])    
    curr = bt
    q.append(curr)
    ret = []
    while q:
        next_level = [] 
        for elem in q:
            if elem.left:
                next_level.append(elem.left)
            if elem.right:
                next_level.append(elem.right)
        ret.append(map(lambda x: x.val, q))
        q = next_level
    return ret

def test():
    t = Tree(1)
    t.right = Tree(3)
    t.left = Tree(2)

    t.left.left = Tree(4)
    t.left.right = Tree(5)

    assert bt_level(t) == [[1], [2, 3], [4, 5]]

    t.right.left = Tree(6)
    t.right.right = Tree(7)

    assert bt_level(t) ==  [[1], [2, 3], [4, 5, 6, 7]]

if __name__ == "__main__":
    test()

