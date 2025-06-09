class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                last = stack.pop()
                if last == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += last * 2
       
        return stack[-1]