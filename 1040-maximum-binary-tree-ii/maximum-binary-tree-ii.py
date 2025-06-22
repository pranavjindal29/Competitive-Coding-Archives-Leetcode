class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val>root.val:
            t=TreeNode(val)
            t.left=root
            return t
        root.right=self.insertIntoMaxTree(root.right,val)
        return root