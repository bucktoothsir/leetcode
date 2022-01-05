class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root:
            first_queue = [root]
            second_queue = []
            while len(first_queue):
                val_list = []
                while len(first_queue):
                    p = first_queue[0]
                    first_queue = first_queue[1:]
                    if p:
                        val_list.append(p.val)
                        second_queue.append(p.left)
                        second_queue.append(p.right)
                if val_list:
                    res.append(val_list)
                val_list = []
                first_queue = second_queue
                second_queue = []
        return res