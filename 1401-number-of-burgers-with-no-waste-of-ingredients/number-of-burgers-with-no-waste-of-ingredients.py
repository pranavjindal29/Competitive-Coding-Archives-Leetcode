class Solution:
    def numOfBurgers(self, T: int, C: int) -> List[int]:
        return [[T//2 - C, 2*C - T//2],[]][T % 2 or T < 2*C or 4*C < T]