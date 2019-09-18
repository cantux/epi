
#!/usr/bin/env python

# decomp given two nodes find the lowest common ancestor.
# 

    
def lca(tree, node0, node1):
    lst1 = get_l(tree, node0)
    lst2 = get_l(tree, node1)

    c = 0
    while lst1 and lst2:
        if lst1[c] != lst2[c]:
            return lst[c - 1]


def get_l(tree, node):
    lst = []
    get_l_helper(tree, node)
    return lst

def get_l_helper(tree, node, lst):

    if tree == node:
        return True

    if get_l_helper(node.right):
        lst.append(node)
        return True
    if get_l_helper(node.left):
        lst.append(node)
        return True
    return False
    


def test():


if __name__ == "__main__":
    test()

