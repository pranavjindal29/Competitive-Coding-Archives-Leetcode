class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n < 2 or m < 2: 
            return 1
        
        row = [[0] * (m + 1) for _ in range(n)]
        col = [[0] * m for _ in range(n + 1)]
        d1 = [[0] * (m + 2) for _ in range(n + 1)]
        d2 = [[0] * (m + 2) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[i+1][j] = col[i][j] + grid[i][j]
                d1[i+1][j+1] = d1[i][j] + grid[i][j]
                d2[i+1][j] = d2[i][j+1] + grid[i][j]

        for k in range(min(n, m), 1, -1):
            for r in range(n - k + 1):
                for c in range(m - k + 1):
                    target = row[r][c+k] - row[r][c]

                    if d1[r+k][c+k] - d1[r][c] != target: 
                        continue
                    if d2[r+k][c] - d2[r][c+k] != target: 
                        continue

                    match = True
                    for i in range(k):
                        if row[r+i][c+k] - row[r+i][c] != target:
                            match = False
                            break
                    if not match: 
                        continue

                    for j in range(k):
                        if col[r+k][c+j] - col[r][c+j] != target:
                            match = False
                            break
                    
                    if match: 
                        return k
        return 1