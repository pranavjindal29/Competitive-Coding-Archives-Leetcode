class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0]) 
        
        graph = dict()
        for i in range(m):
            for j in range(n):
                if   grid[i][j] == 1: graph[i, j] = [(i, j-1), (i, j+1)]
                elif grid[i][j] == 2: graph[i, j] = [(i-1, j), (i+1, j)]
                elif grid[i][j] == 3: graph[i, j] = [(i, j-1), (i+1, j)]
                elif grid[i][j] == 4: graph[i, j] = [(i+1, j), (i, j+1)]
                elif grid[i][j] == 5: graph[i, j] = [(i-1, j), (i, j-1)]
                else:                 graph[i, j] = [(i-1, j), (i, j+1)] 
        

        stack = [(0, 0)]
        seen = set()
        while stack:
            i, j = stack.pop()
            if i == m-1 and j == n-1: return True 
            seen.add((i, j)) 
            for ii, jj in graph[i, j]: 
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen and (i, j) in graph[ii, jj]: 
                    stack.append((ii, jj))
        return False 