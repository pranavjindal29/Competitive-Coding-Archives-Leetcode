class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int("".join(bin(i+1)[2:] for i in range(n)), 2) % (10**9+7)