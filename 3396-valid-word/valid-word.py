class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 3:
            return False

        vowels = 0
        consonants = 0
        vowel_set = "aeiouAEIOU"

        for c in s:
            if c.isalpha():
                if c in vowel_set:
                    vowels += 1
                else:
                    consonants += 1
            elif not c.isdigit():
                return False  # invalid character

        return vowels >= 1 and consonants >= 1