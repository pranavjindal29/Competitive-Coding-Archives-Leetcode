class Solution:
    def countVowelStrings(self, n: int) -> int:
        res = 1
        j = 1
        for i in range(5, 5+n):
            res = (res*i)//j
            j += 1
        return res