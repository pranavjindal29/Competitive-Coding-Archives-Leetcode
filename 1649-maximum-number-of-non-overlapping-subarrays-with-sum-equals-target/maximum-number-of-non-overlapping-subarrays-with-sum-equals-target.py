class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        f={}
        f[0]=1;s=0;ans=0
        for j in nums:
            s+=j
            if s-target in f:ans+=1;f={}
            f[s]=1
        return ans
        