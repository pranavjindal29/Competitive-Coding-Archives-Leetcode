class Solution:
    def __init__(self):
        self.memo = {}

    def solve(self, n: int) -> int:
        if n == 1:
            return 0  # Base case: no operations needed for n == 1
        if n in self.memo:
            return self.memo[n]  # Return memoized result

        even = float('inf')
        odd_minus = float('inf')
        odd_plus = float('inf')

        if n % 2 == 0:
            even = 1 + self.solve(n // 2)
        else:
            odd_minus = 1 + self.solve(n - 1)
            odd_plus = 1 + self.solve(n + 1)

        # Take the minimum of all possible operations
        result = min(even, odd_minus, odd_plus)
        self.memo[n] = result  # Memoize the result
        return result

    def integerReplacement(self, n: int) -> int:
        return self.solve(n)