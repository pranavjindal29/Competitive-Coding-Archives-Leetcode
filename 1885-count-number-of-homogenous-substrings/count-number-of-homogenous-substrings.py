class Solution:
    def countHomogenous(self, s: str) -> int:
        res, l = 0, 0

        for r, c in enumerate(s):
            if c == s[l]:
                res += r - l + 1
            else:
                l = r
                res += 1

        return res % (pow(10, 9) + 7)