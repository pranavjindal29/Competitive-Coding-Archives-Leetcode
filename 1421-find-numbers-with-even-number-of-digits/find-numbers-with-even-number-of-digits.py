class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(int(floor(log10(x))+1)%2==0 for x in nums)
        