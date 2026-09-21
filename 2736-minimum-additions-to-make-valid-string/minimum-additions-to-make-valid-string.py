class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        i = 0
        res = 0
        while i < n:
            count = 0
            if word[i] == 'a':
                count += 1
                i += 1
            if i < n and word[i] == 'b':
                count += 1
                i += 1
            if i < n and word[i] == 'c':
                count += 1
                i += 1
            res += 3 - count
        return res