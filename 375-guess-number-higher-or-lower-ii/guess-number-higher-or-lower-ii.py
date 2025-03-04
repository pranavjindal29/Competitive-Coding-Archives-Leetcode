class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        def calculate_cost(start, end):
            if start >= end:
                return 0
            if dp[start][end] != 0:
                return dp[start][end]

            min_cost = float('inf')

            for guess in range((start + end) // 2, end + 1):
                cost = guess + max(calculate_cost(start, guess - 1), calculate_cost(guess + 1, end))
                min_cost = min(min_cost, cost)

            dp[start][end] = min_cost
            return min_cost

        return calculate_cost(1, n)