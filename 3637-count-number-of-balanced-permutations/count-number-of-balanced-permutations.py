from functools import lru_cache
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        M = 10**9 + 7
        cnt = [0] * 10
        for ch in num:
            cnt[int(ch)] += 1

        n = len(num)
        s = sum(int(ch) for ch in num)
        if s % 2:
            return 0

        left_s = [0] * 10
        left_c = [0] * 10
        r1 = [1] * 11
        ls = lc = 0
        for i in range(9, -1, -1):
            ls += i * cnt[i]
            lc += cnt[i]
            left_s[i] = ls
            left_c[i] = lc
            r1[i] = r1[i + 1] * comb(left_c[i], cnt[i]) % M

        @lru_cache(None)
        def dfs(i, s, c):
            if s == 0 and c == 0:
                return r1[i]
            if i == 10 or s > left_s[i] or c > left_c[i]:
                return 0
            res = 0
            a = s
            for x in range(cnt[i] + 1):
                y = cnt[i] - x
                if a < 0 or c < x or y > left_c[i] - c:
                    a -= i
                    continue
                b = dfs(i + 1, a, c - x) * comb(c, x) % M
                res = (res + b * comb(left_c[i] - c, y)) % M
                a -= i
            return res

        return dfs(0, s // 2, n // 2)