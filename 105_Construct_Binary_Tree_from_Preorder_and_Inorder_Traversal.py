class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder and len(preorder) == len(inorder):
            val = preorder[0]
            idx_in = inorder.index(val)
            left_inorder = inorder[:idx_in]
            right_inorder = inorder[idx_in+1:]
            left_preorder = preorder[1:1+len(left_inorder)]
            right_preorder = preorder[1+len(left_inorder):]
            root = TreeNode(val)
            root.left = self.buildTree(left_preorder, left_inorder)
            root.right = self.buildTree(right_preorder, right_inorder)
            return root
        return None