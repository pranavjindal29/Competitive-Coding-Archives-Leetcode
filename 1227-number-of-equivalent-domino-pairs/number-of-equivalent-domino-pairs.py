class Solution:
    def cantor_pair(self, a: int, b: int) -> int:
        x, y = min(a, b), max(a, b)
        sum_xy = x + y
        return (sum_xy * (sum_xy + 1)) // 2 + y

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        freq = {}
        for a, b in dominoes:
            pair_value = self.cantor_pair(a, b)
            count += freq.get(pair_value, 0)
            freq[pair_value] = freq.get(pair_value, 0) + 1
        return count