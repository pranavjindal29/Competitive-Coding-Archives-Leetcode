"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        a=[]
        if not root:
            return None
        q=deque([root])
        while q:
            size=len(q)
            b=[]
            for i in range(size):
                node=q.popleft()
                b.append(node.val)
                if node.children:
                    q.extend(node.children)
            a.append(b)
        return a