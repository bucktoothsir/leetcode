class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(root: Optional[TreeNode], up, down) -> bool:
            if not root:
                return True
            if root.val >= up or root.val <= down:
                return False
            return help(root.left, min(root.val, up), down) and help(root.right, up, max(root.val, down))
        up = 2 ** 31 
        down = -2 ** 31 - 1
        return help(root, up, down)