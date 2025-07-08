class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        def dfs(vertex: int, color: int, cnt: int) -> None:
            edges = redEdges if color == 0 else blueEdges
            for u, v in edges:
                if vertex == u and steps[1 - color][v] > cnt + 1:
                    steps[1 - color][v] = cnt + 1
                    dfs(v, 1 - color, cnt + 1)

        steps = [[inf] * n, [inf] * n]
        steps[0][0] = steps[1][0] = 0
        dfs(0, 0, 0)
        dfs(0, 1, 0)
        return [min(a, b) if min(a, b) < inf else -1 for a, b in zip(*steps)]