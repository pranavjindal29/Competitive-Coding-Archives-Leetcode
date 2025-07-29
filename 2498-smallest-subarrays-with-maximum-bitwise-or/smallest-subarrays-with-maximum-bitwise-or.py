class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0] * n
        for i in range(n):
            x = nums[i]
            answer[i] = 1
            j = i - 1
            while j >= 0 and nums[j] | x != nums[j]:
                answer[j] = i - j + 1
                nums[j] |= x
                j -= 1
        return answer