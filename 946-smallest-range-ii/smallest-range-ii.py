class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0

        nums.sort()
        res = nums[-1] - nums[0]  

        for i in range(n - 1):
            maxi = max(nums[-1] - k, nums[i] + k)
            mini = min(nums[0] + k, nums[i + 1] - k)
            res = min(res, maxi - mini)

        return res