class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bitmasks = [0] * n
        lengths = [len(word) for word in words]

        for i, word in enumerate(words):
            for ch in word:
                bitmasks[i] |= (1 << (ord(ch) - ord('a')))
        
        max_product = 0

        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0:
                    max_product = max(max_product, lengths[i] * lengths[j])
        
        return max_product