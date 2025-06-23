class Solution:
    def queryString(self, s: str, n: int) -> bool:

        for num in range(n//2+1, n+1):
            if bin(num)[2:] not in s: return False

        return True