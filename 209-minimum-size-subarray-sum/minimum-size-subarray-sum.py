class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1

        n = len(nums)
        min_len = float("inf")
        p1 = 0
        curr_sum = 0

        for p2 in range(n):
            curr_sum += nums[p2]

            while curr_sum >= target:
                min_len = min(p2 - p1 + 1, min_len)
                curr_sum -= nums[p1]
                p1 += 1
        
        return min_len if min_len != float("inf") else 0