class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n, mod=len(nums), 10**9+7
        nums.sort()
        l, r=0, n-1
        ans=0
        while l<=r:
            if nums[l]+nums[r]<=target:
                ans+=(1<<(r-l))
                if ans>=mod: ans%=mod
                l+=1
            else:
                #r-=1
                r=bisect.bisect_right(nums, target-nums[l], lo=l, hi=r)-1
        return ans
        