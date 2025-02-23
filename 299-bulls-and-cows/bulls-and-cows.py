class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bull = 0
        cow = 0
        guess_list = list(guess)

        # First pass: Count bulls
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1
                guess_list[i] = "#"

        # Second pass: Count cows
        for i in range(n):
            if secret[i] != guess[i] and secret[i] in guess_list:
                cow += 1
                guess_list[guess_list.index(secret[i])] = "#"

        return f"{bull}A{cow}B"