class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(dict)

        for (x,y), value in zip(equations, values):
            graph[x][y]=value
            graph[y][x]=1/value
        
        ans = []
        def bfs(start,end):
            if not(start in graph and end in graph):
                return -1.0

            queue = deque([(start, 1.0)])
            visited = set()
            while(queue):
                xx = queue.popleft()
                node = xx[0]
                value = xx[1]
                visited.add(node)
                if node == end:
                    return value

                for i in graph[node]:
                    if i not in visited:
                        queue.append((i,value*graph[node][i]))
            return -1.0
                    
        for i in queries:
            ans.append(bfs(i[0],i[1]))
        
        return ans
        