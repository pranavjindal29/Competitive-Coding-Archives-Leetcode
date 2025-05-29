class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m=len(edges1)+1, len(edges2)+1
        adj1=[[] for _ in range(n)]
        adj2=[[] for _ in range(m)]
        mod2=[False]*n

        def build_adj(edges, adj):
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
        def dfs(i, parent, isEven, adj):
            cnt=isEven
            mod2[i]=isEven
            for j in adj[i]:
                if j==parent: continue
                cnt+=dfs(j, i, not isEven, adj)
            return cnt
        def dfs0(i, parent, isEven, adj):
            cnt=isEven
            for j in adj[i]:
                if j==parent: continue
                cnt+=dfs0(j, i, not isEven, adj)
            return cnt
        build_adj(edges1, adj1)
        build_adj(edges2, adj2)
        y=dfs0(0, -1, True, adj2)
        x=dfs(0, -1, True, adj1)

        cnt2=max(y, m-y)
        cnt=((n-x)+cnt2, x+cnt2)
        return [cnt[b] for b in mod2]


        