class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder, i, bound):
            if (i[0] == len(preorder)) or preorder[i[0]] >= bound:
                return None 
            root = TreeNode(preorder[i[0]])
            i[0] += 1
            root.left = helper(preorder, i, root.val)
            root.right = helper(preorder, i, bound)
            return root
        
        i = [0]
        return helper(preorder, i, float("inf"))