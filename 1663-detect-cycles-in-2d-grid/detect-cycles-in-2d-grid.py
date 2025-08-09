class Solution:
    MOVES = frozenset({
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    })

    def containsCycle(self, grid: list[list[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        visited = set()

        def dfs(i: int, j: int, prev_i: int, prev_j: int) -> bool:
            if (i, j) in visited:
                return False

            visited.add((i, j))

            for di, dj in self.MOVES:
                next_i = i + di
                next_j = j + dj

                if not (0 <= next_i < n and 0 <= next_j < m):
                    continue

                if grid[i][j] != grid[next_i][next_j]:
                    continue

                if prev_i == next_i and prev_j == next_j:
                    continue

                if (next_i, next_j) in visited:
                    return True

                if dfs(next_i, next_j, i, j):
                    return True

            return False

        for row in range(n):
            for col in range(m):
                if dfs(row, col, row, col):
                    return True

        return False