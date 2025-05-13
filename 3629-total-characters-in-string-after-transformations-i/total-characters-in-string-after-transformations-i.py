class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 1000000007
        cnt = [0] * 26
        
        for char in s:
            cnt[ord(char) - ord('a')] += 1

        for _ in range(t):
            tmp = [0] * 26
            for i in range(26):
                if i == 25:
                    tmp[0] = (tmp[0] + cnt[i]) % MOD
                    tmp[1] = (tmp[1] + cnt[i]) % MOD
                else:
                    tmp[i + 1] = (tmp[i + 1] + cnt[i]) % MOD
            cnt = tmp

        return sum(cnt) % MOD