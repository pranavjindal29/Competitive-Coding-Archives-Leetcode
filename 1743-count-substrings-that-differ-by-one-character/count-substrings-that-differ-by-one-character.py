class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp0 = [[0]*(n+1) for _ in range(m+1)] # 0-mismatch
        dp1 = [[0]*(n+1) for _ in range(m+1)] # 1-mismatch
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]: 
                    dp0[i+1][j+1] = 1 + dp0[i][j]
                    dp1[i+1][j+1] = dp1[i][j]
                else: 
                    dp0[i+1][j+1] = 0
                    dp1[i+1][j+1] = 1 + dp0[i][j]
                ans += dp1[i+1][j+1]
        return ans 