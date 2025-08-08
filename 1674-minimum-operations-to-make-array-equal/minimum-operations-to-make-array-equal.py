class Solution:
    def minOperations(self, n: int) -> int:
        return (n * n) // 4 if n % 2 == 0 else ((n * n -1) // 4)