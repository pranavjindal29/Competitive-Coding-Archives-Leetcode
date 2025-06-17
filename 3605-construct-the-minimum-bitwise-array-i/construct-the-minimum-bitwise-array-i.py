class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            for j in range(i):
                if j | (j + 1) == i:
                    ans.append(j)
                    break
            else:
                ans.append(-1)
        return ans