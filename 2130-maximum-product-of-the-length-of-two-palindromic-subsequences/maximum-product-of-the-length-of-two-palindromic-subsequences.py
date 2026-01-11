class Solution:
    def maxProduct(self, s: str) -> int:

        n, d = len(s), defaultdict(int)

        for mask in range(1<<n):
            sub = [s[i] for i in range(n) if mask & (1<<i)]     

            if sub == sub[::-1]: d[mask] = len(sub)

        return max(d[mask1] * d[mask2] for mask1, mask2
                    in combinations(d,2) if mask1 & mask2 == 0) 