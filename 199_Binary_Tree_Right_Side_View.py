class Solution:
    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            node_list = [root]
            while len(node_list):
                next_node_list = []
                for p in node_list:
                    if p.left:
                        next_node_list.append(p.left)
                    if p.right:
                        next_node_list.append(p.right)
                res.append(p.val)
                node_list = next_node_list
        return res
    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            depth = 1
            stack = []
            p = root
            while len(stack) or p:
                while p:
                    stack.append((p, depth))
                    if depth > len(res):
                        res.append((p.val))
                    p = p.right
                    depth += 1
                p, depth = stack.pop()
                p = p.left
                depth += 1
        return res