class Solution:
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        res = [] 
        if root:
            res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            res.extend(self.inorderTraversal(root.right))
        return res        
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if root:
            stack = list()
            p = root
            while len(stack) or p:
                while p:
                    stack.append(p)
                    p = p.left
                p = stack.pop()
                res.append(p.val)
                p = p.right
        return res
                