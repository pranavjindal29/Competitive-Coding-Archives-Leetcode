from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(source, visited, adj, path):
            nonlocal unique
            path.append(source)
            # print(path)
            if hasApple[source]:
                for i in range(len(path)-1,0,-1):
                    if (path[i-1], path[i]) not in unique:
                        unique.add((path[i-1], path[i]))
                    else:
                        break
            for nbr in adj[source]:
                if nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr, visited, adj, path.copy())
        path = []
        unique = set()
        adj = defaultdict(list)
        for edge in edges:
            u, v = edge
            adj[u] += [v]
            adj[v] += [u]
        visited = set()
        visited.add(0)
        dfs(0, visited, adj, path)
        # print(unique)
        return 2 * len(unique)
