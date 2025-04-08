class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        max_diff = [0] * n

        for i in range(n - 1, -1, -1):
            max_diff[i] = nums[i]
            for j in range(i + 1, n):
                max_diff[j] = max(nums[i] - max_diff[j], nums[j] - max_diff[j - 1])
        
        return max_diff[n - 1] >= 0