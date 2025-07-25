class Solution:
    def maxSum(self, nums: List[int]) -> int:
        M=max(nums)
        if M<=0: return M
        seen, Sum=0, 0
        for x in nums:
            if x>=0 and (seen>>x)&1==0:
                Sum+=x
                seen|=(1<<x)
        return Sum

        