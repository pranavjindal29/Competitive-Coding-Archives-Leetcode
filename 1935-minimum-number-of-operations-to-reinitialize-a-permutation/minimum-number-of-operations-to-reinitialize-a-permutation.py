class Solution:
    def reinitializePermutation(self, n: int) -> int:
        k, res = 1, 0
        while True:
            k <<= 1
            res += 1
            if k >= n:
                k -= n - 1
                if k == 1:
                    break
        return res