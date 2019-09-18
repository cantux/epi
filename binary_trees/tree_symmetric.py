#!/usr/bin/env python

lst = []

def tbs(tree):
    tbs(tree.right)

    tbs(tree.left)
    
    return False

def test():
  assert 1 == 1

if __name__ == "__main__":
  test()

