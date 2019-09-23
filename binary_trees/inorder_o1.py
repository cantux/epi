
#!/usr/bin/env python

from successor import succ, ino, create_tree

def ino_p(t):
    ret = []
    curr = t
    while curr.left:
        curr = curr.left
    while curr:
        ret.append(curr)
        curr = succ(curr)

    return ret

def test():
    tree = create_tree()
    assert ino(tree) == ino_p(tree)

if __name__ == "__main__":
    test()

