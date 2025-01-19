class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        st = set()
        n = len(nums)
        if n<4:
            return []
        nums.sort()
        for i in range(n):
            for j in range(i+1, n):
                k,l=j+1,n-1
                while k<l:                    
                        sum = nums[i]+nums[j]+nums[k]+nums[l]
                        if sum == target:
                            st.add((nums[i],nums[j],nums[k],nums[l]))
                            k += 1
                        if sum < target:
                            k += 1
                        else:
                            l -= 1
        li = list(st)
        return li