from math import isqrt
from collections import defaultdict
from functools import lru_cache

MODULO = 10**9 + 7

class Solution:
    def idealArrays(self, array_length: int, max_value: int) -> int:
    
        def generate_primes(limit):
            is_prime = [True] * (limit + 1)
            primes = []
            for num in range(2, limit + 1):
                if is_prime[num]:
                    primes.append(num)
                    for multiple in range(num * num, limit + 1, num):
                        is_prime[multiple] = False
            return primes

        def build_factor_map(prime_list, limit):
            factor_map = defaultdict(list)
            prime_count = len(prime_list)

   
            for idx, prime in enumerate(prime_list):
                factor_map[prime] = [0] * prime_count
                factor_map[prime][idx] = 1

            for value in range(3, limit + 1):
                if value not in factor_map:
                    factor_map[value] = [0] * prime_count
                    for idx, prime in enumerate(prime_list):
                        if value % prime == 0:
                            factor_map[value] = factor_map[value // prime].copy()
                            factor_map[value][idx] += 1
                            break

            return factor_map

        @lru_cache(None)
        def calculate_combinations(x, y):
            if y == 0:
                return 1
            if y == 1:
                return x
            if y > x:
                return 0
            return (calculate_combinations(x - 1, y) + calculate_combinations(x - 1, y - 1)) % MODULO


        primes = generate_primes(max_value)
        factor_map = build_factor_map(primes, max_value)


        total_arrays = 0
        for value in range(1, max_value + 1):
            factors = factor_map[value]
            combinations_product = 1
            for factor_count in factors:
                if factor_count > 0:
                    combinations_product *= calculate_combinations(factor_count + array_length - 1, min(array_length - 1, factor_count))
                    combinations_product %= MODULO
            total_arrays = (total_arrays + combinations_product) % MODULO

        return total_arrays