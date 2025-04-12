class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.res = 0
        nums = [i for i in range(1, n+1)]
        
        def dfs(nums: list, i: int = 1):
            if i == n+1: 
                self.res += 1
                return
            
            for j, num in enumerate(nums):
                if not(num % i and i % num):
                    dfs(nums[:j] + nums[j+1:], i+1)
            
        dfs(nums)
        return self.res