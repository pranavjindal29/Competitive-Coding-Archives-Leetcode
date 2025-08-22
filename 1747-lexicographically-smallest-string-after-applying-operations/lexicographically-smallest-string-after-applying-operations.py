class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        N = 20
        M = n + 2
        f = [[""] * N for _ in range(M)]

        def add(s, a):
            res = ""
            for i, d in enumerate(s):
                if i & 1:
                    res += chr((ord(d) - ord('0') + a) % 10 + ord('0'))
                else:
                    res += d
            return res
        
        def rotate(s, b):
            return s[b : ] + s[0 : b]

        ans = s
        f[0][0] = s

        for i in range(1, N):
            f[0][i] = add(f[0][i - 1], a)
            ans = min(ans, f[0][i])
        for i in range(1, M):
            f[i][0] = rotate(f[i - 1][0], b)
            ans = min(ans, f[i][0])
        
        for i in range(1, M):
            for j in range(1, N):
                s1 = add(f[i][j - 1], a)
                s2 = rotate(f[i - 1][j], b)
                f[i][j] = min(s1, s2)
                ans = min(ans, f[i][j])
                
        return ans