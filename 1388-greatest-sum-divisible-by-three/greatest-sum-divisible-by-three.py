class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp,n = {} , len(nums)
        
        def recursion(index,mod):
            if index == n: 
                return 0 if mod == 0 else -inf
            if (index,mod) in dp: return dp[(index,mod)]
            a = recursion(index + 1, (mod + nums[index]) % 3) + nums[index]
            b = recursion(index + 1 , mod)
            ans = max(a,b)
            dp[(index,mod)] = ans
            return ans
        return recursion(0,0)