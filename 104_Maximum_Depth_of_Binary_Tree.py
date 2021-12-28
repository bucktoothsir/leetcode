def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    return 1 + max(left_depth, right_depth)