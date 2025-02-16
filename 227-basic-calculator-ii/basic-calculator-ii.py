class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_operator = '+'
        
        for i in range(len(s) + 1):
            ch = s[i] if i < len(s) else '\0'
            
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if not ch.isdigit() and ch != ' ' or i == len(s):
                if prev_operator == '+':
                    stack.append(num)
                if prev_operator == '-':
                    stack.append(-num)
                if prev_operator == '*':
                    stack.append(stack.pop() * num)
                if prev_operator == '/':
                    stack.append(int(stack.pop() / num))
                
                prev_operator = ch
                num = 0
        
        return sum(stack)