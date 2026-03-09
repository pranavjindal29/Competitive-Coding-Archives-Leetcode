class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = [[nums[0], 0]]
        steps = 0
        for num in nums[1:]:
            temp = 0
            while stack and stack[-1][0] <= num:
                temp = max(temp, stack[-1][1])
                stack.pop()
            if stack:
                temp += 1
            else:
                temp = 0
            steps = max(steps, temp)
            stack.append([num, temp])
        return steps