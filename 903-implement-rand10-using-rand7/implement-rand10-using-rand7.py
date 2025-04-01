class Solution:
    def rand10(self):

        while True:
            num = (rand7() - 1) * 7 + rand7()
            
            if num <= 40:
                break
        
        return num % 10 + 1