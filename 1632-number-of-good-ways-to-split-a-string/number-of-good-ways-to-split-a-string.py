class Solution:
    def numSplits(self, s: str) -> int:
        if not s: return 0
        total = 0

        prefix_count = [0]*len(s)
        unique = set()
        for i in range(len(s)):
            unique.add(s[i])
            prefix_count[i] = len(unique)

        unique.clear()
        for j in range(len(s) - 1, 0, -1):
            unique.add(s[j])
            if prefix_count[j-1] == len(unique):
                total += 1
            
        return total        