class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int, pathSum = 0) -> TreeNode:
        if not root: return None
        if not root.left and not root.right:
            if pathSum + root.val < limit:
                return None
            return root
        root.left = self.sufficientSubset(root.left, limit, pathSum + root.val)
        root.right = self.sufficientSubset(root.right, limit, pathSum + root.val)
        if not root.left and not root.right:
            return None
        return root
        