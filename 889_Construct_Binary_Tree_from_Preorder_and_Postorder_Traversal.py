class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if preorder and len(preorder) == len(postorder):
            val = preorder[0]
            root = TreeNode(val)
            set_of_left_pre = set()
            set_of_left_post = set()
            idx = 1
            while idx < len(preorder):
                set_of_left_pre.add(preorder[idx])
                set_of_left_post.add(postorder[idx-1])
                if set_of_left_pre == set_of_left_post:
                    break
                idx += 1
            root.left = self.constructFromPrePost(preorder[1:idx+1], postorder[0:idx])
            root.right = self.constructFromPrePost(preorder[idx+1:], postorder[idx:-1])
            return root
        return None
        