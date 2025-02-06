class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)

        currMax = nums[0]
        currMin = nums[0]
        maxProd = nums[0]

        for i in range(1, n):
            temp = max(nums[i], nums[i] * currMax, nums[i] * currMin)
            currMin = min(nums[i], nums[i] * currMax, nums[i] * currMin)
            currMax = temp
            maxProd = max(maxProd, currMax)

        return maxProd
        