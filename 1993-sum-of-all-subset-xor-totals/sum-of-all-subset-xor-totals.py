class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(or_, nums)<<(len(nums)-1)