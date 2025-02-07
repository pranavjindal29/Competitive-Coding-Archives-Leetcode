class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n=len(queries)
        ans=[0]*n
        mp={}
        color=defaultdict(int)
        i=0
        for x, c in queries:
            if x in mp:
                c0=mp[x]
                color[c0]-=1
                if color[c0]==0:
                    color.pop(c0)
            mp[x]=c
            color[c]+=1
            ans[i]=len(color)
            i+=1
        return ans
        