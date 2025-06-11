class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [word for word in words
                if len(word) == len(pattern) and
                len(set(word)) == len(set(pattern)) and
                len(set(zip(word, pattern))) == len(set(word))]