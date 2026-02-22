class Solution:
    def countHousePlacements(self, n: int) -> int:
        @cache
        def f(i):
            if i >= n:
                return 1
            q1 = f(i+1)
            q2 = f(i+2)
            return (q1 + q2)%(10**9+7)
        return pow(f(0), 2, 10**9+7)