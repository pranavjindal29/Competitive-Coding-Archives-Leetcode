class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
                        
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
                