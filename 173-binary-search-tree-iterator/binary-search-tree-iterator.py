# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        self.index = -1
        self.helper(root)
    def helper(self,root):
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.res.append(curr.val)
                curr = curr.right

    def next(self) -> int:
        self.index+=1
        return self.res[self.index]
        

    def hasNext(self) -> bool:
        if self.index<len(self.res)-1:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()