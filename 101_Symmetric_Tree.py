class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def help(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and help(p.left, q.right) and help(p.right, q.left)
        if not root:
            return True 
        else:
            return help(root.left, root.right)