class Solution:
  def longestUnivaluePath(self, root: TreeNode) -> int:
    self.max_len = 0
    def helper(node: TreeNode, parent_val: int) -> int:
        if not node:
            return 0
        
        left_len = helper(node.left, node.val)
        right_len = helper(node.right, node.val)
        
        self.max_len = max(self.max_len, left_len + right_len)
        
        return 1 + max(left_len, right_len) if node.val == parent_val else 0
    
    helper(root, None)
    return self.max_len