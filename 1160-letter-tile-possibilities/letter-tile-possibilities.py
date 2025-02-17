class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = [0] * 26
        fac = [1] * (len(tiles) + 1)
        for i in range(1, len(tiles) + 1):
            fac[i] = i * fac[i - 1]
        for c in tiles:
            counts[ord(c) - ord('A')] += 1
        lengthcounts = [0] * (len(tiles) + 1)
        lengthcounts[0] = 1
        for i in range(26):
            if counts[i] > 0:
                temp = [0] * (len(tiles) + 1)
                for j in range(len(tiles) + 1):
                    if lengthcounts[j] > 0:
                        for k in range(1, counts[i] + 1):
                            totallength = j + k
                            temp[totallength] += lengthcounts[j] * fac[totallength] // (fac[k] * fac[j])
                for j in range(len(tiles) + 1):
                    lengthcounts[j] += temp[j]
        return sum(lengthcounts[1:])