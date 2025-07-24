class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hour_degree = (hour % 12) * 30 + (minutes / 60) * 30
        minute_degree = minutes * 6

        larger_degree = max(hour_degree, minute_degree)
        smaller_degree = min(hour_degree, minute_degree)

        return min(larger_degree - smaller_degree, 360 - (larger_degree - smaller_degree))