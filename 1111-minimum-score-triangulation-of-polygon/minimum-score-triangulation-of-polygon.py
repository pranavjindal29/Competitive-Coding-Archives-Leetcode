class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(pos1: int, pos2: int) -> int:
            if pos2 - pos1 <= 1:
                return 0
            ans = inf
            for pos in range(pos1 + 1, pos2):
                ans = min(ans, dp(pos1, pos) + dp(pos, pos2) + values[pos1] * values[pos2] * values[pos])
            return ans

        return dp(0, len(values) - 1)