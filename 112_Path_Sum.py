class Solution:
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == targetSum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val) 
    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum-root.val)]
        while stack:
            p, targetSum = stack.pop()
            if not p.left and not p.right:
                if targetSum == 0:
                    return True
            if p.right:
                stack.append((p.right, targetSum-p.right.val))
            if p.left:
                stack.append((p.left, targetSum-p.left.val))
        return False
        
        