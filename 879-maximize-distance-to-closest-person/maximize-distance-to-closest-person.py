class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, prev, L = 0, -1, len(seats)
        for i, n in enumerate(seats):
            if n:
                dist = i if prev == -1 else (i - prev)//2
                res = max(res, dist)
                prev = i
                
        if not seats[i]: 
            res = max(res, i - prev)

        return res