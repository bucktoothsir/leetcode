class Solution:
    def preorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            res.append(root.val)
            res.extend(self.preorderTraversal(root.left))
            res.extend(self.preorderTraversal(root.right))
        return res
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            stack = [root]
            while len(stack):
                p = stack.pop()
                res.append(p.val)
                if p.right:
                    stack.append(p.right)
                if p.left:
                    stack.append(p.left)
        return res
               