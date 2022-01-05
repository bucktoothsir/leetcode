class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def help(root):
            if not root:
                return 0
            left = help(root.left)
            right = help(root.right)
            mid = 0
            if root.val == p.val or root.val == q.val:
                mid = 1
            if mid + left + right >= 2:
                self.ans = root
            return left or right or mid
        help(root)
        return self.ans