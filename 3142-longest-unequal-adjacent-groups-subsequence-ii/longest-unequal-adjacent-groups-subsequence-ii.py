class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        connections = {}
        maxs = {}
        result = []

        def HammingDistance(base, word):
            differences = 0
            
            if len(base) != len(word):
                return -1
            else:
                for i in range(len(word)):
                    if base[i] != word[i]: differences += 1
                    if differences > 2: return -1
            return differences

        for i in range(n):
            connections[i] = []
            for k in range(i, n):
                if groups[i] != groups[k] and HammingDistance(words[i], words[k]) == 1:
                    connections[i].append(k)
        
        for i in range(n - 1, -1, -1):
            maxs[i] = []

            for connection in connections[i]:
                if len(maxs[connection]) > len(maxs[i]):
                    maxs[i] = maxs[connection]
            
            maxs[i] = [words[i]] + maxs[i]
            if len(maxs[i]) > len(result):
                result = maxs[i]

        return result
                    


