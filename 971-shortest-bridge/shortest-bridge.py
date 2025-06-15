class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        front = []
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    front.append([x, y])
                    grid[x][y] = 2
                    break
            if front:
                break
        
        boundary = []
        while front:
            sx, sy = front.pop()
            for x, y in [[sx + 1, sy], [sx - 1, sy], [sx, sy + 1], [sx, sy - 1]]:
                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y] == 1:
                        front.append([x, y])
                        grid[x][y] = 2
                    elif grid[x][y] == 0:
                        boundary.append([x, y])
                        grid[x][y] = 2
        
        distance = 0
        while True:
            distance += 1
            front = []
            for sx, sy in boundary:
                for x, y in [[sx + 1, sy], [sx - 1, sy], [sx, sy + 1], [sx, sy - 1]]:
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return distance
                        elif grid[x][y] == 0:
                            front.append([x, y])
                            grid[x][y] = 2
            boundary = front

        return distance

