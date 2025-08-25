from collections import defaultdict
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        starts, ends, zero_moves = defaultdict(int), defaultdict(int), defaultdict(int)
        N = len(nums)
        for i in range(N // 2):
            x, y = nums[i], nums[N-i-1]
            starts[min(x, y)+1] += 1
            ends[max(x,y)+limit] += 1
            zero_moves[x+y] += 1
        result = float('inf')
        intervals = 0
        for target in range(2, 2*limit+1):
            intervals += starts[target]
            cost = N - intervals - zero_moves[target]
            result = min(cost, result)
            intervals -= ends[target]
        return result