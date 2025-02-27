from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        maxLen = 0

        for curr in range(2, n):
            start, end = 0, curr - 1
            while start < end:
                pairSum = arr[start] + arr[end]
                if pairSum > arr[curr]:
                    end -= 1
                elif pairSum < arr[curr]:
                    start += 1
                else:
                    dp[end][curr] = dp[start][end] + 1
                    maxLen = max(dp[end][curr], maxLen)
                    end -= 1
                    start += 1

        return 0 if maxLen == 0 else maxLen + 2