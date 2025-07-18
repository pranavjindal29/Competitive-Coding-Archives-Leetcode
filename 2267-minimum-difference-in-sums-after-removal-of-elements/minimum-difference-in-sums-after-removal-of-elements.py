class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)//3
        diff=[0]*(n+1)
        heapify(pqL:=[-x for x in nums[:n]])
        heapify(pqR:=nums[2*n:])
        Sum=sum(nums[:n])
        ans=Sum
        for i in range(n, 2*n+1):
            diff[i-n]=Sum
            x=nums[i]
            if x>=-pqL[0]: continue
            Sum+=x+pqL[0]
            heapreplace(pqL, -x)
        Sum=sum(nums[2*n:])
        ans-=Sum
        for i in range(2*n-1, n-2, -1):
            diff[i-n+1]-=Sum
            ans=min(ans, diff[i-n+1])
            x=nums[i]
            if x<=pqR[0]: continue
            Sum+=x-pqR[0]
            heapreplace(pqR, x)
        return ans
        