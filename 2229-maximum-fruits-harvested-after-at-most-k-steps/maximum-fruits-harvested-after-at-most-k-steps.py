class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ans = rsm = ii = 0 
        for i, (p, x) in enumerate(fruits): 
            if p > startPos + k: break 
            rsm += x
            if p <= startPos: fn = lambda ii: startPos - fruits[ii][0]
            else: fn = lambda ii: min(2*(p-startPos) + (startPos-fruits[ii][0]), (p-startPos) + 2*(startPos-fruits[ii][0]))
            while ii <= i and fn(ii) > k: 
                rsm -= fruits[ii][1]
                ii += 1
            ans = max(ans, rsm)
        return ans 