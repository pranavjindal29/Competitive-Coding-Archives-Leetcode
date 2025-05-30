class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n=len(edges)
        inf=1<<32
        dist1=[inf]*n
        dist2=[inf]*n
        def dfs(node, dist):
            d, i=0, node
            while i!=-1 and dist[i]==inf:
                dist[i]=d
                d+=1
                i=edges[i]
        dfs(node1, dist1)
        dfs(node2, dist2)
        minD, index=inf, -1
        for i in range(n):
            max12=max(dist1[i], dist2[i])
            if max12<minD: 
                minD=max12
                index=i
        return index

        