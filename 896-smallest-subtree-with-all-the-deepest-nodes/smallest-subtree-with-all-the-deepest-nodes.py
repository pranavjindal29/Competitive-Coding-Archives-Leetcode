# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = None
        self.maxDepth = -1

    def dfs(self, root, depth):
        if not root:
            self.maxDepth = max(self.maxDepth, depth)
            return depth
        left = self.dfs(root.left, depth + 1)
        right = self.dfs(root.right, depth + 1)
        if left == right and left == self.maxDepth:
            self.res = root
        return max(left, right)

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        return self.res