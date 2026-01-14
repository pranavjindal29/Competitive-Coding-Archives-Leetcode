class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        tally, ans = 1, 0
        triangle = lambda x: x * (x + 1)//2

        for p1, p2 in pairwise(prices):
            if p1 - p2 == 1:
                tally+= 1
            else:
                ans+= triangle(tally)
                tally = 1
                
        ans+= triangle(tally)

        return  ans