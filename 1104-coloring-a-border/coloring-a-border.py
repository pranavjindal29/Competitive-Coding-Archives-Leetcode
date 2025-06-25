class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows, columns = len(grid), len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque([(row, col)])
        targetColor = grid[row][col]
        visited[row][col] = True

        while queue:
            x, y = queue.popleft()
            visited[x][y] = True

            if x==rows-1 or x==0 or y==columns-1 or y==0: 
                grid[x][y] = color

            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0<=nx<rows and 0<=ny<columns and not visited[nx][ny]:
                    if (grid[nx][ny] != targetColor):
                        grid[x][y] = color
                    else:
                        queue.append((nx, ny))
        return grid