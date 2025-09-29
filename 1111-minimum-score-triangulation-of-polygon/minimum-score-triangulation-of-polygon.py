class Solution:
    def minScoreTriangulation(self, v: List[int]) -> int:
        n=len(v)
        if n==3: return v[0]*v[1]*v[2]
        dp=[[0]*n for _ in range(n-1)]

        for d in range(2, n):
            for i in range(n-d):
                j=i+d
                w, e=1<<32, v[i]*v[j]
                for k in range(i+1, j):
                    w=min(w, e*v[k]+dp[i][k]+dp[k][j])
                dp[i][j]=w
        return dp[0][-1]