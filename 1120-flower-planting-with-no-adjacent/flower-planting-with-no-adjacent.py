class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        d, ans = defaultdict(list), [0]*(n+1)
      
        for a, b in paths: d[a].append(b) ; d[b].append(a)
         
        for i in range(1,n+1):
            ans[i] = ({1,2,3,4}-{ans[node] for node in d[i]}).pop()
            
        return ans[1:]