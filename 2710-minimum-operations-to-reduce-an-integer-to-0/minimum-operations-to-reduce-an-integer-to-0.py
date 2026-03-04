class Solution:
    def minOperations(self, n: int) -> int:
        dp = [0] * (n+1)

        for i in range(1, n+1):
            p = 1
            while p < i:
                p <<= 1
            if p == i:
                dp[i] = 1
            dp[i] = 1+ min(dp[p-i], dp[i-(p>>1)])

        return dp[n]