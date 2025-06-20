class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
      
      if not root:
        return False
      
      self.ans = []
      self.idx = 0
      
      def recurse(node):
        if not node:
          return True
        
        if node.val != voyage[self.idx]:
          return False
        
        self.idx += 1
        if node.left and (node.left.val != voyage[self.idx]):
          if node.right:
            self.ans.append(node.val)
          return recurse(node.right) and recurse(node.left)
        
        else:
          return recurse(node.left) and recurse(node.right)
        
      if recurse(root):
        return self.ans
      return [-1]