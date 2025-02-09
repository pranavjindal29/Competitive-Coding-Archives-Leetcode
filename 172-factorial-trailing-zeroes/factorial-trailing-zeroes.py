class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        i = 5
        while i <= n:
            fives += n // i
            i *= 5
        return fives