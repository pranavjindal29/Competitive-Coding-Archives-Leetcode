class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n=len(nums)
        cnt, xM=0, 0
        for x in nums:
            if cnt==0: xM=x
            cnt+=(x==xM)*2-1

        cntL, cntR, i=0, 0, 0
        while i<n and cntL*2<=i:
            cntL+=nums[i]==xM
            i+=1
        i-=1
        for j in range(i+1, n):
            cntR+=nums[j]==xM
    
        return i if cntR*2>(n-i-1) else -1
        