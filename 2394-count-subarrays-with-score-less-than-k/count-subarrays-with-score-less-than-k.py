class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        start = 0
        sum_ = 0
        count = 0
        
        for end in range(len(nums)):
            sum_ += nums[end]
            
            while sum_ * (end - start + 1) >= k:
                sum_ -= nums[start]
                start += 1
            
            count += (end - start + 1)
        
        return count