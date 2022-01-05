class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        if root:
            stack = []
            q = root
            while len(stack) or q:
                while q:
                    if p.val == q.val:
                        if q.right:
                            q = q.right
                            while q.left:
                                q = q.left
                            return q
                        if len(stack):
                            return stack[-1]
                        else:
                            return None
                    stack.append(q)
                    q = q.left
                q = stack.pop()
                q = q.right
        return None
            
        