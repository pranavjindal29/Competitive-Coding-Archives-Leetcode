class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for p in points:
            d = {}
            for q in points:
                dist = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                d[dist] = d.get(dist, 0) + 1
            for k in d:
                count += d[k] * (d[k] - 1)
        return count