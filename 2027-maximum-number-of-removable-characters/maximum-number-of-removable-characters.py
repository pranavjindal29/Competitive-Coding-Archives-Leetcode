class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        mp = {x: i for i, x in enumerate(removable)}
        
        def fn(x):
            k = 0 
            for i, ch in enumerate(s): 
                if mp.get(i, inf) < x: continue 
                if k < len(p) and ch == p[k]: k += 1
            return k == len(p)
        
        lo, hi = -1, len(removable)
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if fn(mid): lo = mid
            else: hi = mid - 1
        return lo 