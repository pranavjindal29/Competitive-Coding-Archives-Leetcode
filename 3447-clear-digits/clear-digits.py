class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)