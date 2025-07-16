class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        ans = 0            
        m = len(mat)
        n = len(mat[0])
        presum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                presum[i][j] = mat[i-1][j-1] + presum[i][j-1] + presum[i-1][j] - presum[i-1][j-1] 
                lo, hi = 1, min(i, j) + 1
                while lo < hi:
                    mid = (lo + hi)//2
                    cursum = presum[i][j] - presum[i-mid][j] - presum[i][j-mid] + presum[i-mid][j-mid]
                    if cursum > threshold:
                        hi = mid
                    else:
                        lo = mid + 1
                ans = max(ans, lo-1)
        return ans