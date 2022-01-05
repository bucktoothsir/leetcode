# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def help(root):
            if not root:
                s = 'null,'
            else:
                s = str(root.val)
                s += ','
                s += help(root.left)
                s += help(root.right)
            return s 
        s = help(root).strip(',')
        return s
            

        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def help():
            if data[0] == 'null':
                data.pop(0)
                return None
            root = TreeNode(data[0])
            data.pop(0)
            root.left = help()
            root.right = help()
            return root
        if data:
            data = data.strip(',').split(',')
            return help()
        return None
                