class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, third = [], float('-inf')
        
        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        return False