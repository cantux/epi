    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # does max diameter necessarily pass from root, no!!
        # then I would like to find the maximum path to the leaf of a certain node
        if not root:
            return 0
        max_diam = [-1]
        def rec(curr):
            if not curr:
                return 0
            
            left_max_depth = rec(curr.left) + 1
            right_max_depth = rec(curr.right) + 1
            
            max_diam[0] = max(left_max_depth + right_max_depth - 1, max_diam[0])
            
            return max(left_max_depth, right_max_depth)
        
        rec(root)
        return max_diam[0] - 1
