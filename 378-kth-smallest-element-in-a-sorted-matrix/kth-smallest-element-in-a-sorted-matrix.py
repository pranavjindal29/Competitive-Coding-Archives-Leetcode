import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countK(mid, smaller, larger):
            n = len(matrix)
            count = 0
            row, col = n - 1, 0
            while row>=0 and col < n:
                if matrix[row][col] > mid:
                    larger = min(larger, matrix[row][col])
                    row -= 1
                else:
                    smaller = max(smaller, matrix[row][col])
                    count += row + 1
                    col += 1
            return count, smaller, larger
        
        n = len(matrix)
        start, end = matrix[0][0], matrix[-1][-1]
        while start < end:
            mid = (start+end)/2
            smaller, larger =  matrix[0][0], matrix[n-1][n-1]
            
            count, smaller, larger = countK(mid, smaller, larger)
            if count == k:
                return smaller
            elif count < k:
                start = larger
            else:
                end = smaller
        
        return start
        