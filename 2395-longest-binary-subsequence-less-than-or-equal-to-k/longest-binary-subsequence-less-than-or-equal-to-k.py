class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        ones = 0
        value = 0
        power = 1

        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if value + power > k:
                    continue
                value += power
                ones += 1
            power <<= 1
            if power > k:
                break
        return zeros + ones