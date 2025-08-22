class Solution:
    def numberOfSets(self, n, k):
        return math.comb(n + k - 1, k * 2) % (10**9 + 7)