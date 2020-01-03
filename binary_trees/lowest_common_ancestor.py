
#!/usr/bin/env python
def lowestCommonAncestor(self, root, p, q):
    if root==None or p==root or q==root:
        return root 
    left=self.lowestCommonAncestor(root.left,p,q)
    right=self.lowestCommonAncestor(root.right,p,q)
    if not left and not right:
        return None
    if not right:
        return left
    if not left:
        return right 
    if left and right:
        return root

if __name__ == "__main__":
    test()

