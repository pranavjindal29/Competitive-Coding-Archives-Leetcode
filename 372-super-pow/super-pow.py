class Solution:
    MOD = 1337

    def pow(self, a: int, b: int) -> int:
        result = 1
        a %= self.MOD  # Taking mod to prevent overflow
        for _ in range(b):
            result = (result * a) % self.MOD
        return result

    def superPow(self, a: int, b: list[int]) -> int:
        result = 1
        for i in range(len(b) - 1, -1, -1):
            result = (result * self.pow(a, b[i])) % self.MOD
            a = self.pow(a, 10)  # Power up for the next iteration
        return result