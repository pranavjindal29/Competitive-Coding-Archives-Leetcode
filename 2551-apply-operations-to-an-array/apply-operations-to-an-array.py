from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        new_nums = [0] * len(nums)
        count = 0
        i = 0

        while i < len(nums) - 1:
            if nums[i] != 0:
                if nums[i] == nums[i + 1]:
                    new_nums[count] = nums[i] * 2
                    i += 1  
                else:
                    new_nums[count] = nums[i]
                count += 1
            i += 1
        
        if i < len(nums) and nums[i] != 0:
            new_nums[count] = nums[i]

        return new_nums