from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        left_max = [0] * n
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])

        right_max = [0] * n
        right_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        ans = 0
        for i in range(1, n - 1):
            left = left_max[i - 1]
            right = right_max[i + 1]
            ans = max(ans, (left - nums[i]) * right)

        return ans