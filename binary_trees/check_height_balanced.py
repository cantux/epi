
#!/usr/bin/env python

def chb(tree):
    if not tree:
        return 0
    
    right = 1 + chb(tree.right) 
    left = 1 + chb(tree.left)

    if abs(left - right) < 2:
        return max(left, right)
    return sys.max_int

def c(tree)
    if chb(tree) < 2:
        return True
    return False

def test():
    assert 1 == 1

if __name__ == "__main__":
    test()

