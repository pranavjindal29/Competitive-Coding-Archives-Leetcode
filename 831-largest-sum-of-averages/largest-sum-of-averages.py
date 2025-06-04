class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dp = [prefix_sum[i] / i for i in range(1, n + 1)]
        
        for j in range(2, k + 1):
            for i in range(n, j - 1, -1):  
                for p in range(j - 1, i):
                    dp[i - 1] = max(dp[i - 1], dp[p - 1] + (prefix_sum[i] - prefix_sum[p]) / (i - p))
        
        return dp[n - 1]