from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, we cannot partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        # The sum we are looking for is half of the total sum
        target = total_sum // 2
        
        # DP array to check if we can achieve the subset sum
        dp = [False] * (target + 1)
        dp[0] = True  # Sum of 0 is always achievable (by taking no elements)
        
        # Iterate through each number in the array
        for num in nums:
            # We iterate backwards to avoid overwriting results from the same iteration
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        # The answer will be true if the target sum is achievable
        return dp[target]