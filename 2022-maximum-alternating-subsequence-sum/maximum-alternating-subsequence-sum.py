class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                ans += nums[i] - nums[i + 1]
        ans += nums[-1]
        return ans