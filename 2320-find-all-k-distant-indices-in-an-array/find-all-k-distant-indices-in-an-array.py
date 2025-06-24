class Solution:
    def findKDistantIndices(self, nums, key, k):
        index = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if nums[j] == key and abs(i - j) <= k:
                    index.append(i)
                    break
        return index