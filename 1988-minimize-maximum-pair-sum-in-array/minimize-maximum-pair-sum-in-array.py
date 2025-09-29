class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        return nums.sort() or max(nums[i]+nums[-1-i] for i in range((len(nums)>>1)+1))