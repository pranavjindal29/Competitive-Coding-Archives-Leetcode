class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle edge cases
        if numerator == 0:
            return "0"
        if denominator == 0:
            return ""

        # Initialize result and check for negative sign
        result = ""
        if (numerator < 0) ^ (denominator < 0):
            result += "-"
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part of the result
        result += str(numerator // denominator)

        # Check if there is a fractional part
        if numerator % denominator == 0:
            return result

        result += "."

        # Use a dictionary to store the position of each remainder
        remainder_dict = {}
        remainder = numerator % denominator

        # Keep adding the remainder to the result until it repeats or the remainder becomes 0
        while remainder != 0 and remainder not in remainder_dict:
            remainder_dict[remainder] = len(result)
            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator

        # Check if there is a repeating part
        if remainder in remainder_dict:
            result = result[:remainder_dict[remainder]] + "(" + result[remainder_dict[remainder]:] + ")"

        return result