class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0
        maxValue = max(nums)
        
        for num in nums:
            if num == maxValue:
                k -= 1
            while k ==0:
                if nums[left] == maxValue:
                    k += 1
                left += 1
                
            result += left
            
        return result        