class Solution:
    def possibleBipartition(self, n: int, dis: List[List[int]]) -> bool:
        
        G, P = defaultdict(set), {}
        for i,j in dis : G[i].add(j), G[j].add(i)
        
        def dfs(i, p):
            if i in P : return P[i] == p
            P[i] = p
            return all(dfs(j, not p) for j in G[i])

        return all(dfs(i, True) for i in range(1,n+1) if i not in P)