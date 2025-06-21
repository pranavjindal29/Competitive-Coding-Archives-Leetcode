class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        res = []
        first = second = 0
        while first < len(firstList) and second < len(secondList):
            left = max(firstList[first][0],secondList[second][0])
            right = min(firstList[first][1],secondList[second][1])

            if left <= right:
                res.append([left,right])
            
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1
        return res