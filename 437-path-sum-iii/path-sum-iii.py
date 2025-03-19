from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1  
        return self.dfs(root, 0, targetSum, prefixSumCount)

    def dfs(self, node, currentSum, targetSum, prefixSumCount):
        if not node:
            return 0

        currentSum += node.val
        count = prefixSumCount[currentSum - targetSum]
        
        prefixSumCount[currentSum] += 1
        
        count += self.dfs(node.left, currentSum, targetSum, prefixSumCount)
        count += self.dfs(node.right, currentSum, targetSum, prefixSumCount)
        
        prefixSumCount[currentSum] -= 1
        if prefixSumCount[currentSum] == 0:
            del prefixSumCount[currentSum]
        
        return count