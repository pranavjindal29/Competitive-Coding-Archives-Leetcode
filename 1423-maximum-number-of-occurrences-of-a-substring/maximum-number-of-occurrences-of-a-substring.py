class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        c = Counter([s[i:i+minSize] for i in range(len(s)-minSize+1)])
      
        return max((c[substr] for substr in c
                      if len(set(substr)) <= maxLetters), default = 0)