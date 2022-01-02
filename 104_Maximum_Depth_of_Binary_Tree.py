def maxDepth1(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

def maxDepth2(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def top_down(root, depth):
        global max_depth
        if not root.left and not root.right:
            max_depth = max(max_depth, depth)
        elif root.left:
            top_down(root.left, depth+1)
        else:
            top_down(root.right, depth+1)
    max_depth = 0
    if root:
        top_down(root, 1)
    return max_depth

        

