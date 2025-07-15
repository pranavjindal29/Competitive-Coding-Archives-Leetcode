class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        s, n = sum(colsum), len(colsum)
        if upper + lower != s: return []
        u, d = [0] * n, [0] * n
        for i in range(n):
            if colsum[i] == 2 and upper > 0 and lower > 0:
                u[i] = d[i] = 1
                upper, lower = upper-1, lower-1
            elif colsum[i] == 1:    
                if upper > 0 and upper >= lower:
                    u[i], upper = 1, upper-1
                elif lower > 0 and lower > upper:
                    d[i], lower = 1, lower-1
                else: return []    
            elif not colsum[i]: continue
            else: return []
        return [u, d] 