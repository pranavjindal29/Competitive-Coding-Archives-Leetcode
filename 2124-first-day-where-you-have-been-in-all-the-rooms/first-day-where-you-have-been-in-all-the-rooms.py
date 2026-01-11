class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n
        mod = int(1e9+7)
        for i in range(n-1):
            dp[i+1] = (dp[i] - dp[nextVisit[i]] + 1 + dp[i] + 1) % mod
        return dp[n-1] 