class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix)
        row = len(matrix[0])
        for i in range(col):
            for j in range(row):
                if matrix[i][j] == target:
                    return True
        return False