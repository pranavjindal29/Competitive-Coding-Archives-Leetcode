class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ''
        for i in range(n):
            q, r = divmod(k, 26)
            if r == 0:
                q -= 1
                r = 26

            if n - q - i >= 2:
                res += 'a'
                k -= 1
            else:
                res += chr(r + 96) + 'z' * (n - i - 1)
                break
        
        return res