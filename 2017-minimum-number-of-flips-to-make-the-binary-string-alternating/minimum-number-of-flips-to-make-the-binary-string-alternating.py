class Solution:
    def minFlips(self, s: str) -> int:
        cnt0 = s[::2].count('0') + s[1::2].count('1')
        cnt1 = len(s) - cnt0
        ans = min(cnt0, cnt1)
        if not len(s) % 2:
            return ans
        for n in s:
            cnt0, cnt1 = cnt1, cnt0
            if n == '1':
                cnt1 += 1
                cnt0 -= 1
            else:
                cnt0 += 1
                cnt1 -= 1
            ans = min(cnt0, cnt1, ans)
        return ans