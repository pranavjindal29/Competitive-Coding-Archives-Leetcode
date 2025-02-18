class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = ""
        stack = []
        
        for i in range(n + 1):
            stack.append(i + 1)
            
            if i == n or pattern[i] == 'I':
                while stack:
                    result += str(stack.pop())
        
        return result