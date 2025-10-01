class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinked, eb = 0, 0
        while numBottles > 0:
            drinked += numBottles
            eb += numBottles
            numBottles = eb // numExchange
            eb = eb % numExchange
        return drinked