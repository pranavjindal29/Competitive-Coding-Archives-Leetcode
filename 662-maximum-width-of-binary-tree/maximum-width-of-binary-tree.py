from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            level_size = len(queue)
            level_start = queue[0][1]
            level_end = queue[-1][1]
            max_width = max(max_width, level_end - level_start + 1)

            for _ in range(level_size):
                node, position = queue.popleft()
                if node.left:
                    queue.append((node.left, position * 2))
                if node.right:
                    queue.append((node.right, position * 2 + 1))

        return max_width