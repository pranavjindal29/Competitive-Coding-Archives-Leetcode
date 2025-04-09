class Solution:
    def minOperations(self, nums, k):
        if k > min(nums):
            return -1

        unique_elements = set(nums)
        unique_count = len(unique_elements)

        if k in unique_elements:
            return unique_count - 1
        else:
            return unique_count