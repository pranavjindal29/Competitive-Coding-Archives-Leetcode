from collections import defaultdict
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counts = defaultdict(int)
        for num in deliciousness:
            counts[num] += 1
        
        numSolutions = 0
        for i in range(22):
            twoPower = 2**i
            
            visited = set()
            for num in deliciousness:
                if num in visited:
                    continue

                complement = twoPower - num
                complementCount = counts[complement]
                if complementCount == 0:
                    continue  
                if num == complement:
                    numSolutions += (complementCount * (complementCount - 1)) // 2
                else:
                    numSolutions += complementCount * counts[num]
                numSolutions %= (10**9) + 7

                visited.add(num)
                visited.add(complement)

        return numSolutions
                