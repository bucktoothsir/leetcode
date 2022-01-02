class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder and len(inorder) == len(postorder):
            val = postorder[-1]
            index_in = inorder.index(val)
            root = TreeNode(val)
            left_inorder = inorder[:index_in]
            right_inorder = inorder[index_in + 1:]
            left_postorder = postorder[:len(left_inorder)]
            right_postorder = postorder[len(left_inorder):-1]
            root.left = self.buildTree(left_inorder, left_postorder)
            root.right = self.buildTree(right_inorder, right_postorder)
            return root
        return None