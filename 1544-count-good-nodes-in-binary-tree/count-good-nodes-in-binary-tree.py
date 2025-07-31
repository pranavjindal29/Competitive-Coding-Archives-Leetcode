class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root,val):
            if root:
                k = solve(root.left, max(val,root.val)) + solve(root.right, max(val,root.val))
                if root.val >= val:
                    k+=1
                return k
            return 0
        return solve(root,root.val)