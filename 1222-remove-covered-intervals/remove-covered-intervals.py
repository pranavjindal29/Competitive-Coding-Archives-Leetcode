class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res, longest = len(intervals), 0
        srtd = sorted(intervals, key = lambda i: (i[0], -i[1]))
        
        for _, end in srtd:
            if end <= longest:
                res -= 1
            else:
                longest = end
                
        return res