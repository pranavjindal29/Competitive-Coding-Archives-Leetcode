class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:

        mat = [set(row) for row in mat]
        
        rSet = set(mat.pop())

        for row in mat: rSet = {m+n for m in row for n in rSet}
        
        return min(abs(n - target) for n in rSet)