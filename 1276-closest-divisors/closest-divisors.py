class Solution:
    def closestDivisors(self, num: int, o=0) -> List[int]:
        for i in range(int(math.sqrt(num)) + 1, 1, -1):
            if (num + 1) % i == 0 or (o := (num + 2) % i == 0):
                return [i, (num + 1 + o) // i]