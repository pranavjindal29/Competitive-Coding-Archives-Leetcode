class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        j = sum(shifts)
        for i in range(len(shifts)):
            c = ord(s[i]) - ord('a')
            c = (c + j)%26
            s[i] = chr(ord('a')+c)
            j -= shifts[i]
        return ''.join(s)        