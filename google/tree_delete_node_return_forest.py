    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        # cases:
        # leaf dleetion, nothin to add
        # node deletion with a single child, child will be added to disjoint set
        # node dleetion with two childs, childs will be added to disjoint set
        
        # here is an important case, how do we handle deletion of already spearated set?
        
        # what edge cases can we have other than that?
        
        # let's run some examples to cover couple situations
        # 1 2 3 4 5 balanced tree
        
        #     1
        #   2   3
        # 4  5
        # when we are given a list 2, 5
        # we must be able to delete the 2 and then 5
        
        # if we delete 2 first, add the resulting disjoints to the result
        # when we encounter 5 we must go in the result array and edit it
        
        # instead if we dleted the bottom nodes first we wouldn't encounter such problem
        # I am thinknig post order traversal might do the trick!
        
        # let's consider that idea for a second.
        
        # sample run 12345 and to_delete:25
        # 1
        #   2
        #       4
        #       curr not in list nothing to do
        #       5
        #       curr in list. 
        #         a) delete the node by removing the parent connection -> means I need to keep a ref to parent node, and also keep if it is left or right # assuming this is a binary tree otherwise we would need to keep an index
        #         b) add the children to disjoing lists
        res = []
        def rec(curr, parent, is_left):
            if not curr:
                return
            rec(curr.left, curr, True)
            rec(curr.right, curr, False)
            
            # do some op here
            if curr.val in to_delete:
                # a
                if parent:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None
                # b
                if curr.left:
                    res.append(curr.left)
                if curr.right:
                    res.append(curr.right)
            
        
        
        rec(root, None, False)
        # for the finishing touch I will add the root node if it is not deleted
        # how can I detect if it is deleted or not?
        if root.val not in to_delete:
            res.append(root)
        return res
