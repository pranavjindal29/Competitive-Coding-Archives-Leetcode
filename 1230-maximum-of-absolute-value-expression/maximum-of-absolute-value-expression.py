class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        for p, q in (1, 1), (1, -1), (-1, 1), (-1, -1): 
            val = low = inf 
            for i, (x, y) in enumerate(zip(arr1, arr2)): 
                ans = max(ans, p*x + q*y + i - low)
                low = min(low, p*x + q*y + i)
        return ans
        
    