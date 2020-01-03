def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    len_n = len(nums)

    def rec(left, right):
        if left > right:
            return None
        mid = left + ((right - left) // 2)
        parent = TreeNode(nums[mid])
        parent.left = rec(left, mid - 1)
        parent.right = rec(mid + 1, right)
        return parent

    return rec(0, len_n - 1)
