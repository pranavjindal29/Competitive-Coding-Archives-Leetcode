class Solution:
    def countNicePairs(self, nums):
        numbers = {}

        for num in nums:
            temporary_number = num - self.reverse(num)

            if temporary_number in numbers:
                numbers[temporary_number] += 1
            else:
                numbers[temporary_number] = 1

        result = 0
        mod = 1000000007
        for value in numbers.values():
            result = (result % mod + (value * (value - 1) // 2)) % mod

        return int(result)

    def reverse(self, number):
        reversed_number = 0
        while number > 0:
            reversed_number = reversed_number * 10 + number % 10
            number //= 10
        return reversed_number