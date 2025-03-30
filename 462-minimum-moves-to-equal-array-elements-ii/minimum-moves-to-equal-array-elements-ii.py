class Solution:
    def minMoves2(self, nums):
        nums.sort()
        start, end, count = 0, len(nums) - 1, 0
        while start < end:
            count += nums[end] - nums[start]
            start += 1
            end -= 1
        return count