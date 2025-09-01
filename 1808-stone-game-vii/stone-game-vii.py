class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = [[-1 for _ in range(len(stones))] for _ in range(len(stones))]
        def stone(tot, i, j):
            if i == j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            left = (tot-stones[i]) - stone(tot-stones[i], i+1, j)
            right = (tot-stones[j]) - stone(tot-stones[j], i, j-1)

            dp[i][j] = max(
                left,
                right
            )

            return dp[i][j]

        return stone(sum(stones), 0, len(stones)-1)
        