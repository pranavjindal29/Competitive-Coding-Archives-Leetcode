class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        minCost = 0

        l, r = 0, 1

        while r < len(colors):
            while r < len(colors) and colors[l] == colors[r]:
                r += 1
            if r - l > 1:
                maxCost = max(neededTime[l:r])
                totalCost = sum(neededTime[l:r])
                minCost += (totalCost - maxCost)
            l = r
        
        return minCost