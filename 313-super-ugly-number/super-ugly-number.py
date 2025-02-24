class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen=(set([1]))
        heap=[1]
        for i in range(n):
            x = heapq.heappop(heap)
            for i in primes:
                ugly = x * i 
                if ugly not in seen:
                    seen.add(ugly)
                    heapq.heappush(heap,ugly)
        return x