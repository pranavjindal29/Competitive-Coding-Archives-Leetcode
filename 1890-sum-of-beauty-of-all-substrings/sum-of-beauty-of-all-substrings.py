class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        a = ord('a')
        for i in range(n):
            cnt = [0]*26
            mx = 0
            for j in range(i, n):
                k = ord(s[j]) - a
                cnt[k] += 1
                if cnt[k] > mx:
                    mx = cnt[k]
                mn = float('inf')
                for c in cnt:
                    if c:
                        mn = min(mn, c)
                ans += mx - mn
        return ans