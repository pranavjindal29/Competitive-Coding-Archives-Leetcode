class Solution:
    def __init__(self):
        self.dp = [-1] * 100005
    
    def solve(self, j, nums):
        if j == len(nums):
            return 1
        if self.dp[j] != -1:
            return self.dp[j]
        c = 0
        if j + 1 < len(nums):
            if nums[j] == nums[j + 1]:
                c |= self.solve(j + 2, nums)
        if j + 2 < len(nums):
            if nums[j] == nums[j + 1] and nums[j] == nums[j + 2]:
                c |= self.solve(j + 3, nums)
            if nums[j] + 1 == nums[j + 1] and nums[j + 1] + 1 == nums[j + 2]:
                c |= self.solve(j + 3, nums)
        self.dp[j] = c
        return c
    
    def validPartition(self, nums):
        self.dp = [-1] * 100005
        return self.solve(0, nums) == 1