class Solution:
    def maxRemovals(self, A: str, B: str, targetIndices: List[int]) -> int:
        n, m = len(A), len(B)
        target = set(targetIndices)

        dp = [-inf] * m + [0]
        for i in range(n - 1, -1, -1):
            for j in range(m + 1):
                dp[j] += i in target
                if j < m and A[i] == B[j]:
                    dp[j] = max(dp[j], dp[j + 1])
        return dp[0]