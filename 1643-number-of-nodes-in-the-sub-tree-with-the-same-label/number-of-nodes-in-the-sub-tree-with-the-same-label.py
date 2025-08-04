class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        visited = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        hashMap = defaultdict(int)
        ans = [0] * n

        def dfs(node):
            tmp = hashMap[labels[node]]
            visited.add(node)
            hashMap[labels[node]] += 1
            for nextNode in graph[node]:
                if nextNode not in visited:
                    dfs(nextNode)
            ans[node] = hashMap[labels[node]] - tmp

        dfs(0)
        return ans
