class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        list = []
        freqS = [0] * 26
        freqP = [0] * 26

        if len(s) < len(p):
            return list

        for i in range(len(p)):
            freqS[ord(s[i]) - ord('a')] += 1
            freqP[ord(p[i]) - ord('a')] += 1

        start = 0
        end = len(p)

        if freqS == freqP:
            list.append(start)

        while end < len(s):
            freqS[ord(s[start]) - ord('a')] -= 1
            freqS[ord(s[end]) - ord('a')] += 1

            if freqS == freqP:
                list.append(start + 1)

            start += 1
            end += 1

        return list