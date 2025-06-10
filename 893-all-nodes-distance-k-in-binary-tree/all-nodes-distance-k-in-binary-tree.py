class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parent = {}
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for _ in range(size):
                top = queue.popleft()

                if top.left:
                    parent[top.left.val] = top
                    queue.append(top.left)

                if top.right:
                    parent[top.right.val] = top
                    queue.append(top.right)

        visited = {}
        queue.append(target)
        while k > 0 and queue:
            size = len(queue)

            for _ in range(size):
                top = queue.popleft()

                visited[top.val] = 1

                if top.left and top.left.val not in visited:
                    queue.append(top.left)

                if top.right and top.right.val not in visited:
                    queue.append(top.right)

                if top.val in parent and parent[top.val].val not in visited:
                    queue.append(parent[top.val])

            k -= 1

        while queue:
            ans.append(queue.popleft().val)

        return ans