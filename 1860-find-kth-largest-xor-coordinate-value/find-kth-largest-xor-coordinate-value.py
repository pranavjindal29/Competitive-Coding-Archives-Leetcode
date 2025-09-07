from random import choice
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        xors = self.construct_xors(matrix)
        return self.quick_select(xors, k)

    def construct_xors(self, xors):
        m = len(xors)
        n = len(xors[0])

        def valid_coord(i, j):
            return 0 <= i < m and 0 <= j < n

        for i in range(m):
            for j in range(n):
                for di, dj in ((-1, 0), (0, -1), (-1, -1)):
                    ci, cj = i + di, j + dj
                    xors[i][j] ^= xors[ci][cj] * valid_coord(ci, cj)
    
        xors = [xor for row in xors for xor in row]
        return xors

    def quick_select(self, container, k):
        pivot = choice(container)

        g = [xor for xor in container if xor > pivot]
        e = [xor for xor in container if xor == pivot]
        l = [xor for xor in container if xor < pivot]

        if len(g) > k:
            return self.quick_select(g, k)
        if len(g) == k:
            return min(g)
        if len(g) + len(e) >= k:
            return e[0]
        if len(g) + len(e) + len(l) > k:
            return self.quick_select(l, k - len(g) - len(e))
        if len(g) + len(e) + len(l) == k:
            return min(l)