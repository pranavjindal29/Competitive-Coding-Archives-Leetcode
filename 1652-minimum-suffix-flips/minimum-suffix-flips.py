class Solution:
    def minFlips(self, target: str) -> int:
        cnt = 0
        for t in target:
            cnt += abs(cnt%2 - int(t))
        return cnt