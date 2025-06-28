from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        nums_with_indices.sort(key=lambda x: -x[0])
        top_k = sorted(nums_with_indices[:k], key=lambda x: x[1])
        return [num for num, _ in top_k]