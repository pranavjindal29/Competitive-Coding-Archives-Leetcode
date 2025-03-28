from queue import PriorityQueue

class Solution:
    def maxPoints(self, grid, queries):
        rows, cols = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        result = [0] * len(queries)
        
        heap = PriorityQueue()
        visited = [[False] * cols for _ in range(rows)]
        
        heap.put((grid[0][0], 0, 0))
        visited[0][0] = True
        points = 0
        
        for query_val, query_idx in sorted_queries:
            while not heap.empty() and heap.queue[0][0] < query_val:
                _, row, col = heap.get()
                points += 1
                
                for dr, dc in DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        not visited[nr][nc]):
                        heap.put((grid[nr][nc], nr, nc))
                        visited[nr][nc] = True
            
            result[query_idx] = points
        
        return result