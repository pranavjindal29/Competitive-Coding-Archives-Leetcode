class Solution:
    def flipLights(self, n: int, m: int) -> int:
        
        def fn(n, m): 
            """Return number of different status."""
            if m * n == 0: return 1
            return fn(n-1, m-1) + fn(n-1, m)
        
        return fn(min(n, 3), min(m, 3))