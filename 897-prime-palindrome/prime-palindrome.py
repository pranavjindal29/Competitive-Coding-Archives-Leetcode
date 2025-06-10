class Solution:
    @staticmethod
    def is_palindrome(x):
        return (s := str(x)) == s[::-1]
    
    @staticmethod
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5 + 1)):
            if not x % i:
                return False
        return True

    def primePalindrome(self, n: int) -> int:
        while True:
            if Solution.is_palindrome(n) and Solution.is_prime(n):
                return n
            n += 1
            if 10**7 < n < 10**8: # There are no prime palindromes in this range
                n = 10**8