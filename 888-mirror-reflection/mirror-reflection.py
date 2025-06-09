class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            q /= 2
            p /= 2
            
        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1