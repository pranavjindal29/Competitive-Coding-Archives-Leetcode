class Solution:
    def __init__(self):
        self.dp = {}

    def solve(self, s, m):
        if not s:
            return True
        if s in self.dp:
            return self.dp[s]
        for i in range(len(s)):
            r = s[:i + 1]
            if r in m:
                if self.solve(s[i + 1:], m):
                    self.dp[s] = True
                    return True
        self.dp[s] = False
        return False

    def wordBreak(self, s, wordDict):
        m = set(wordDict)
        return self.solve(s, m)