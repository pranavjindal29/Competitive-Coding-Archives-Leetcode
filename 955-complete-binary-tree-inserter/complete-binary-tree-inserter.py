class CBTInserter:

    def __init__(self, root: TreeNode):
        self.head=root
        

    def insert(self, v: int) -> int:
        root=self.head
        if root == None:
            root.data=v
            return root.val
        else:
            queue=[root]
            nextqueue=[]

            while queue != []:
                for root in queue:

                    if root.left is  None:
                        root.left=TreeNode(v)
                        return root.val
                    else:
                         nextqueue.append(root.left)      

                    if root.right is None:
                        root.right=TreeNode(v)
                        return root.val
                    else:
                        nextqueue.append(root.right)
                queue=nextqueue
                nextqueue=[]
        

    def get_root(self) -> TreeNode:
        return self.head