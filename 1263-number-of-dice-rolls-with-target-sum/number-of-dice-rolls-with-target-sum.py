class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        t = target - n
        ret = 0
        l = 0
        m = 10**9 + 7
        while l*k <= t:
            r = t - l*k
            ret = (ret + ((-1)**l) * comb(n,l) * comb(r+n-1,n-1)) % m
            l += 1
        return ret