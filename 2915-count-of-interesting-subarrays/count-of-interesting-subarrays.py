class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n=len(nums)
        mp=defaultdict(int)
        mp[0]=1
        ans, prefix=0, 0
        for i, x in enumerate(nums):
            prefix+=(x%modulo==k)
            ans+=mp[(prefix+modulo-k)%modulo]
            mp[prefix%modulo]+=1
        return ans