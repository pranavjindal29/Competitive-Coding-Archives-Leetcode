class Solution:
    def buildAdj(self, matrix, n):
        adj = [[] for _ in range(n)]

        for a,b in matrix:
            adj[a].append((b, True))
            adj[b].append((a, False))
        
        return adj

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        adj = self.buildAdj(connections, n)
        visit = set()

        def dfs(node):
            nonlocal count
            visit.add(node)

            for nei, outgoing in adj[node]:
                if nei not in visit:
                    if outgoing:
                        count += 1
                
                    dfs(nei)
                
        dfs(0)
        return count