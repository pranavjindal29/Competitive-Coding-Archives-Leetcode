class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[n] * n for _ in range(n)]
        
        for x, y in mines:
            grid[x][y] = 0

        for i in range(n):
            l, r, u, d = 0, 0, 0, 0
            for j in range(n):
                l = l + 1 if grid[i][j] != 0 else 0
                r = r + 1 if grid[i][n-j-1] != 0 else 0
                u = u + 1 if grid[j][i] != 0 else 0
                d = d + 1 if grid[n-j-1][i] != 0 else 0
                
                grid[i][j] = min(grid[i][j], l)
                grid[i][n-j-1] = min(grid[i][n-j-1], r)
                grid[j][i] = min(grid[j][i], u)
                grid[n-j-1][i] = min(grid[n-j-1][i], d)
        
        return max(map(max, grid))