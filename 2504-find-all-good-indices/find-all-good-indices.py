class Solution:
    def goodIndices(self, a: List[int], k: int) -> List[int]:
        n, ans= len(a) ,[]
        dp1 , dp2= [1]*(n+1), [1]*(n+1)
        for i in range(1,n):
            if a[i-1]>=a[i]:  dp1[i]= dp1[i-1]+1
        
        for i in range(n-2,-1,-1):
            if a[i]<=a[i+1]:  dp2[i]= dp2[i+1]+1
        
        for i in range(k,n-k):
            if dp1[i-1]>=k and dp2[i+1]>=k: ans+= [i]
        return ans