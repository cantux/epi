    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # is it sufficient to check max and min depths of a node and if their heights are not one away, return False
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1
