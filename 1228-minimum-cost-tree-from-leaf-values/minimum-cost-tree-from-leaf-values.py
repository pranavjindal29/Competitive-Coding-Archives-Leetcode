class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.helper(arr, 0, len(arr) - 1, {})
        
    def helper(self, arr, l, r, cache):
        if (l, r) in cache:
            return cache[(l, r)]
        if l >= r:
            return 0
        
        res = float('inf')
        for i in range(l, r):
            rootVal = max(arr[l:i+1]) * max(arr[i+1:r+1])
            res = min(res, rootVal + self.helper(arr, l, i, cache) + self.helper(arr, i + 1, r, cache))
        
        cache[(l, r)] = res
        return res