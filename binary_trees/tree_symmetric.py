#!/usr/bin/env python

lst = []

def tbs(tree):
    if not root:return True
    def sym(l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False

        if l.val == r.val:
            return sym(l.left, r.right) and sym(l.right, r.left)
        return False
    
    return sym(root.left, root.right)

def test():
  assert 1 == 1

if __name__ == "__main__":
  test()

