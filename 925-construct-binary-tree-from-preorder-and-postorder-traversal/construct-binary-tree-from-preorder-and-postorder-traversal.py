# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for val in preorder:
            dic[val] = TreeNode(val)
        
        while postorder:
            node = postorder[0]
            idx = preorder.index(node)
            parent = preorder[idx - 1]
            if idx-1 < 0:
                return dic[node]
            if not dic[parent].left:
                dic[parent].left = dic[node]
            else:
                dic[parent].right = dic[node]
            
            postorder = postorder[1:]
            preorder = preorder[:idx] + preorder[idx+1:]

        return dic[node]