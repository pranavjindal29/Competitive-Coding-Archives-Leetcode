class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        
        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                result[left] = nums[i]
                left += 1
            
            if nums[j] > pivot:
                result[right] = nums[j]
                right -= 1
        
        while left <= right:
            result[left] = pivot
            left += 1
            
        return result