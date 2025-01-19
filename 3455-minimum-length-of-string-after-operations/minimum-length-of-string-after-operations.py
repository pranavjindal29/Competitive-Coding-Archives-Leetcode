class Solution:
    def minimumLength(self, s: str) -> int:
        char_frequency = [0] * 26
        total_length = 0
        for char in s:
            char_frequency[ord(char) - ord('a')] += 1
        for frequency in char_frequency:
            if frequency == 0:
                continue
            if frequency % 2 == 0:
                total_length += 2
            else:
                total_length += 1
        return total_length