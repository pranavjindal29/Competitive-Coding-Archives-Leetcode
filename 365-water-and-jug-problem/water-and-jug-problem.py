
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        x = self.gcd(jug1Capacity, jug2Capacity)
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        return targetCapacity % x == 0

    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a