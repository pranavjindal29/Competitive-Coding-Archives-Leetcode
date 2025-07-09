class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
       
        left_count = 0
        right_count = 0
        
        def dfs(node):
            nonlocal left_count, right_count  
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # Check if the current node is Player 1's x
            if node.val == x:
                left_count = left  
                right_count = right  
            
            return left + right + 1
        
      
        dfs(root)

        # Check all possible options 
        if left_count > n // 2 or right_count > n // 2 or (n - (left_count + right_count + 1)) > n // 2:
            return True
        
        return False