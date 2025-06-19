class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        is_null_in_between_nodes = False
        while queue:
            total_nodes_in_level = len(queue)
            for i in range(total_nodes_in_level):
                curr_node = queue.popleft()
                if curr_node is None:
                    is_null_in_between_nodes = True
                else:
                    if is_null_in_between_nodes:
                        return False
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
        return True