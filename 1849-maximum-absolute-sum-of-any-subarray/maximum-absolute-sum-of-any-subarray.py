class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(0, max(K:=list(accumulate(nums))))-min(0, min(K))
        
        