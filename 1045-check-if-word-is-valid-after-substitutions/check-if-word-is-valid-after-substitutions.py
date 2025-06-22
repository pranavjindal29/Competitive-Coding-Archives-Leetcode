class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            stack.append(char)
            while len(stack)>2 and stack[-3:] == ['a', 'b', 'c']:
                stack[-3:] = []
            
        return  not stack



