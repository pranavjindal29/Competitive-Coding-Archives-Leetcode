
from collections import defaultdict
import heapq
import sys
sys.setrecursionlimit(10**6)

MOD = 10**9 + 7

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(src):
            distance = [float("inf")] * (n + 1)
            distance[src] = 0
            queue = [(0, src)]
            while queue:
                dist, node = heapq.heappop(queue)
                if dist > distance[node]:
                    continue
                for neighbor, weight in graph[node]:
                    new_dist = dist + weight
                    if new_dist < distance[neighbor]:
                        distance[neighbor] = new_dist
                        heapq.heappush(queue, (new_dist, neighbor))
            return distance
        
        distance = dijkstra(n)
        
        dp = [-1] * (n + 1)

        def count_paths(node):
            if node == n:  
                return 1
            if dp[node] != -1:  
                return dp[node]

            total_paths = 0

            for neighbor, weight in graph[node]:
                if distance[neighbor] < distance[node]:
                    total_paths += count_paths(neighbor)
                    total_paths %= MOD  

            dp[node] = total_paths  
            return dp[node]
        
        return count_paths(1)