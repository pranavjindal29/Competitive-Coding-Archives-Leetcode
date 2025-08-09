class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (1<<30)%n==0
        