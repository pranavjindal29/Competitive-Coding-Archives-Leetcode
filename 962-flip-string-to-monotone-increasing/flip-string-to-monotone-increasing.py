class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero = 0
        one = 0
        totalzeroes = 0
        n = len(s)
        mn = float('inf')

        res = [0] * n

        for i in s:
            if i == '0':
                totalzeroes += 1

        for i in range(n):
            if s[i] == '0':
                zero += 1

            res[i] = one + totalzeroes - zero

            if s[i] == '1':
                one += 1
            if mn > res[i]:
                mn = res[i]
        return mn