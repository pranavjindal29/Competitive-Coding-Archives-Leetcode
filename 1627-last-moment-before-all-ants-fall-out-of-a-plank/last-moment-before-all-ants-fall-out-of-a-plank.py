class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if len(right) == 0:
            return n - (n - max(left))
        if len(left) == 0:
            return n - min(right)
        return max(n - (n - max(left)), n - min(right))