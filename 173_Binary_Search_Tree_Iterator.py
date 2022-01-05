class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.p = root
        self.stack = []
        while self.p:
            self.stack.append(self.p)
            self.p = self.p.left
        self.p = self.stack.pop()
        
    def next(self) -> int:
        val = self.p.val
        if self.p.right:
            self.p = self.p.right
            while self.p:
                self.stack.append(self.p)
                self.p = self.p.left
        if len(self.stack): 
            self.p = self.stack.pop()
        else:
            self.p = None
        return val

    def hasNext(self) -> bool:
        return self.stack or self.p
        
