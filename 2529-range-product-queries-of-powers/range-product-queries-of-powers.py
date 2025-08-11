class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod=10**9+7
        B30=(1<<30)-mod
        def pow2mod(exp):
            if exp<30: return 1<<exp
            q,r=divmod(exp, 30)
            B=pow(B30, q, mod)
            return B*(1<<r)%mod
        exp2=[]
        for i in range(30):
            if (n>>i) & 1:
                exp2.append(i)
        
        exp2=list(accumulate(exp2, initial=0)) # 1-indexed prefix sum
        
        m=len(queries)
        ans=[0]*m
        for i, (s, e) in enumerate(queries):
            ans[i]=pow2mod(exp2[e+1]-exp2[s])
        return ans
        