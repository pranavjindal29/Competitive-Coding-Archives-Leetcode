class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return max(self.longestSubstring(t,k) for t in split(f'[{q}]',s)) if (q:=''.join(c for c,f in Counter(s).items() if f<k)) else len(s)