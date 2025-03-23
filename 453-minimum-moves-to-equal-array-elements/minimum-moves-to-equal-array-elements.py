class Solution:
    def minMoves(self, nums):
        min_element = min(nums)
        return sum(num - min_element for num in nums)