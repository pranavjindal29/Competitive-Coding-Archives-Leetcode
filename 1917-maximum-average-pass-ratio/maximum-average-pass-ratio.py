class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calc_ratio(t, p): 
            return (t - p) / (t * (t + 1))

        ratio = [(-1 * calc_ratio(t, p), t, p) for p, t in classes]
        heapq.heapify(ratio)

        while extraStudents:
            _, t, p = heapq.heappop(ratio)
            p += 1
            t += 1
            heapq.heappush(ratio, (-1 * calc_ratio(t, p), t, p))
            extraStudents -= 1

        return sum(x[2] / x[1] if x[1] != 0 else 1 for x in ratio) / len(ratio)