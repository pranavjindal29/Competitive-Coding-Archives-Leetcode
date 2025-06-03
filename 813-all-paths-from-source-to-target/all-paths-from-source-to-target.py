class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        def dfs(current,end,comb):
            if current==end:
                ans.append(comb[:])
                return
            for node in graph[current]:
                comb.append(node)
                dfs(node,end,comb)
                comb.pop()
        dfs(0,len(graph)-1,[0])
        return ans



        