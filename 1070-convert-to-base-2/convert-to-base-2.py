class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        
        a = ""
        while n != 0:
            r = n % 2
            a = str(r) + a
            n = -(n // 2)
        return a