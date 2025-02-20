class Solution:
    def findDifferentBinaryString(self, nums):
        result = []
        for i in range(len(nums)):
            if nums[i][i] == '0':
                result.append('1')
            else:
                result.append('0')
        return ''.join(result)