class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: No children
            if not root.left and not root.right:
                return None
            
            # Case 2: One child
            if not root.left or not root.right:
                return root.left if root.left else root.right
            
            # Case 3: Two children
            temp = root.left
            while temp.right:
                temp = temp.right
            root.val = temp.val
            root.left = self.deleteNode(root.left, temp.val)

        return root