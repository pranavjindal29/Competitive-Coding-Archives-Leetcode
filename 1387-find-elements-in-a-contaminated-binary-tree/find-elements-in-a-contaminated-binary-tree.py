class FindElements:
    def __init__(self, root: TreeNode):
        self.values = set()
        
        def recover(node, val):
            if not node:
                return
            node.val = val
            self.values.add(val)
            recover(node.left, 2 * val + 1)
            recover(node.right, 2 * val + 2)
        
        recover(root, 0)
    
    def find(self, target: int) -> bool:
        return target in self.values