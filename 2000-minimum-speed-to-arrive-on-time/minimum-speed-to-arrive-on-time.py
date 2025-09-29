class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def can_reach_on_time(speed):
            total_time = sum( ((d + speed - 1) // speed) for d in dist[:-1]) + dist[-1] / speed
            return total_time <= hour
        left, right = 1, 10**7
        while left < right:
            mid = (left + right) // 2
            if can_reach_on_time(mid):
                right = mid
            else:
                left = mid + 1
        
        if can_reach_on_time(left):
            return left
        else:
            return -1