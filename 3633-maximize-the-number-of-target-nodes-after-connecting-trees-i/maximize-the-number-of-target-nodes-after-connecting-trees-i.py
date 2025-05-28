from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_graph(edges):
            n = len(edges) + 1
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def bfs_count_max(graph, max_dist):
            n = len(graph)
            result = [0] * n
            for start in range(n):
                visited = [False] * n
                q = deque()
                q.append((start, 0))
                visited[start] = True
                count = 1
                while q:
                    node, dist = q.popleft()
                    if dist == max_dist:
                        continue
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append((neighbor, dist + 1))
                            count += 1
                result[start] = count
            return result

        g1 = build_graph(edges1)
        g2 = build_graph(edges2)

        if k == 0:
            return [1] * len(g1)

        cnt1 = bfs_count_max(g1, k)
        cnt2 = bfs_count_max(g2, k - 1)
        max_cnt2 = max(cnt2)

        return [cnt + max_cnt2 for cnt in cnt1]