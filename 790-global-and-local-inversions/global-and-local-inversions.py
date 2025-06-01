class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if(nums[i]==i or nums[i]-1==i or nums[i]+1==i):
                continue
            else:
                return False
        return True