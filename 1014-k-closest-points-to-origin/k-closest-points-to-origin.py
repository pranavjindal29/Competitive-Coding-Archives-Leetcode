class Solution:
    def kClosest(self, A, k):

        q = []

        for x, y in A:

            heapq.heappush(q, [-(x*x + y*y), [x, y]])
            
            if len(q) > k:
                heapq.heappop(q)

        res = []
        while q:
            _, points = heapq.heappop(q)
            res.append(points)
        return res