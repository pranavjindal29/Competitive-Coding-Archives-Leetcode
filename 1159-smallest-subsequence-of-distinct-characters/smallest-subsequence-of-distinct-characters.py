class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {char:i for i,char in enumerate(s)}
        stack = []
        seen = set()
        for i,char in enumerate(s):
            if char in seen: continue
            while stack and char < stack[-1] and last[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)