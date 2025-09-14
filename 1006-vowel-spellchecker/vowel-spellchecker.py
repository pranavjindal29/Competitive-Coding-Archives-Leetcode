class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        original = set(wordlist)
        caseMap = {}
        vowelMap = {}

        def changeVowel(word: str) -> str:
            return "".join("*" if ch in "aeiou" else ch for ch in word)

        for w in wordlist:
            lower = w.lower()
            caseMap.setdefault(lower, w)
            vowelMap.setdefault(changeVowel(lower), w)

        res = []
        for q in queries:
            lower = q.lower()
            cv = changeVowel(lower)

            if q in original:
                res.append(q)
            elif lower in caseMap:
                res.append(caseMap[lower])
            elif cv in vowelMap:
                res.append(vowelMap[cv])
            else:
                res.append("")
        return res