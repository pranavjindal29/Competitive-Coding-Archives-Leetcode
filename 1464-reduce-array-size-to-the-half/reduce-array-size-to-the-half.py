from collections import Counter

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counts = sorted(Counter(arr).values(), reverse=True)
        removed = 0
        target = len(arr) // 2
        cnt = 0
        for c in counts:
            removed += c
            cnt += 1
            if removed >= target:
                return cnt
        return cnt