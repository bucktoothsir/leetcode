class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def help(root):
            if not root.left and not root.right:
                self.res += 1
                return True
            flag = 1
            if root.left:
                flag_left = help(root.left)
                flag = flag and flag_left and root.left.val == root.val
            if root.right:
                flag_right = help(root.right)
                flag = flag and flag_right and root.right.val == root.val
            self.res += flag
            return flag
        if root:
            flag = 0
            help(root)
        return self.res
           
            
                    