class Solution:
    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            res.extend(self.postorderTraversal(root.left))
            res.extend(self.postorderTraversal(root.right))
            res.append(root.val)
        return res
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            stack = []
            p = root
            while len(stack) or p:
                while p:
                    stack.append(p)
                    p = p.left
                p = stack.pop()
                if p.right:
                    stack.append(p)
                    q = p
                    p = p.right
                    q.right = None
                else:
                    res.append(p.val)
                    p = None
        return res

        