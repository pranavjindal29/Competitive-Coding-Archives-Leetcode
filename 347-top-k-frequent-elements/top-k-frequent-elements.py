from collections import Counter
from heapq import nlargest
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = Counter(nums)
        return nlargest(k, diction.keys(), key=diction.get)