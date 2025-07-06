from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        total = 0
        for k, v in freq.items():
            group_size = k + 1
            groups = ceil(v / group_size)
            total += groups * group_size
        return total