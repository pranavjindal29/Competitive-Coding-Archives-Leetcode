class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        num_idx = {num: i for i, num in enumerate(nums)}
        nums.sort(reverse=True)
        head = TreeNode(val=nums[0])
        for num in nums[1:]:
            node = head
            while node:
                if num_idx[num] > num_idx[node.val]:
                    if not node.right:
                        node.right = TreeNode(val=num)
                        break
                    else:
                        node = node.right
                else:
                    if not node.left:
                        node.left = TreeNode(val=num)
                        break
                    else:
                        node = node.left
            
        return head