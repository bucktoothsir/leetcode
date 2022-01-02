class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            node_queue = [root]
            while len(node_queue):
                next_node_queue = []
                for i in range(len(node_queue)):
                    p = node_queue[i]
                    if p.left:
                        next_node_queue.append(p.left)
                    if p.right:
                        next_node_queue.append(p.right)
                    if i < len(node_queue) - 1:
                        q = node_queue[i+1]
                        p.next = q
                        p = p.next
                node_queue = next_node_queue
        return root
