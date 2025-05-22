class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        width = 1
        height = 1

        def calculate_width_height(node, w, h):
            nonlocal height, width
            if node.left or node.right:
                w = (w*2) + 1
                width = max(w, width)

            height = max(height, h)
            if node.left:
                calculate_width_height(node.left, w, h+1)

            if node.right:
                calculate_width_height(node.right, w, h+1)

        calculate_width_height(root, 1, 1)

        matrix = [["" for _ in range(width)] for _ in range(height)]

        def populate_matrix(node, min_range, max_range, row):
            col = min_range + (max_range - min_range)//2
            matrix[row][col] = str(node.val)

            if node.left:
                populate_matrix(node.left, min_range, col - 1, row + 1)
            if node.right:
                populate_matrix(node.right, col + 1, max_range, row + 1)

        populate_matrix(root, 0, width, 0)
        return matrix