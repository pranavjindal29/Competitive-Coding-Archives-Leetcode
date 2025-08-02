class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        dp = [float("inf")] * (len(arr) + 1)
        start, end = 0, 0
        subarray_sum = 0
        answer = float("inf")
        min_length = float("inf")
        prefix_sum = {0 : -1}
        while end < len(arr):
            subarray_sum += arr[end]
            if subarray_sum - target in prefix_sum:
                start = prefix_sum[subarray_sum - target]
                answer = min(answer, dp[start + 1] + end - start)
                min_length = min(min_length, end - start)
            dp[end + 1] = min_length
            prefix_sum[subarray_sum] = end
            end += 1
        return -1 if answer == float("inf") else answer