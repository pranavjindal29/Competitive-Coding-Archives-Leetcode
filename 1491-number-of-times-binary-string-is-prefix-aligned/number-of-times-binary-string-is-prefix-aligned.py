class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        largest_bit = 0
        count = 0
        for i, bit in enumerate(flips, 1):
            largest_bit = max(largest_bit, bit)
            if largest_bit == i:
                count += 1
        return count