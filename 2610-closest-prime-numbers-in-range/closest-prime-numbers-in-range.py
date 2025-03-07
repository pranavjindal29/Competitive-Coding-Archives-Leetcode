class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, right + 1, i):
                    sieve[j] = False
        
        primes = [i for i in range(left, right + 1) if sieve[i]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        result = [-1, -1]
        
        for i in range(1, len(primes)):
            gap = primes[i] - primes[i-1]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i-1], primes[i]]
        
        return result