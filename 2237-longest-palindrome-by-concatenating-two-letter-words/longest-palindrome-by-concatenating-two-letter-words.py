class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Solution 2: Fewer lookups & w/o mutating the counter
        cnt, res = Counter(words), 0
        for w, c in cnt.items(): # Address non-palindromic pairs
            rev = w[::-1]
            if w < rev and rev in cnt:
                res += 4 * min(c, cnt[rev])

        for w, c in cnt.items(): # Address palindromic words in pairs
            if w[0] == w[1]:     # palindromic word like 'aa'
                res += 4 * (c // 2)

        # Check and potentially add one palindromic word in center
        if any(w[0] == w[1] and cnt[w] % 2 for w in cnt):
            res += 2
            
        return res



        # Solution 1: First thought, don't like mutation of counter
        cnt, length = Counter(words), 0
        center_used = False
        for w, c in list(cnt.items()):
            rev = w[::-1]
            if w == rev:
                pairs = c // 2
                length += pairs * 4
                if c % 2 and not center_used:
                    length += 2
                    center_used = True
            else:
                if rev in cnt:
                    take = min(c, cnt[rev])
                    length += take * 4
                    cnt[rev] -= take
                    cnt[w] = 0
        return length