class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        def get_sum(sr, sc, s):
            side = s // 2
            r = sr + side
            c = sc
            if side == 0:
                return grid[r][c]
            res = 0
            for dr,dc in (-1,1),(1,1),(1,-1),(-1,-1):
                for i in range(side):
                    r += dr
                    c += dc
                    res += grid[r][c]
            return res
        
        R,C = len(grid), len(grid[0])
        MAX_SIZE = min(R, C) 
        MAX_SIZE -= MAX_SIZE % 2 == 0
        min_heap = []
        for s in range(1, MAX_SIZE + 1, 2): 
            for sc in range(C - s + 1): 
                for sr in range(R - s + 1): 
                    cur_sum = get_sum(sr, sc, s)
                    if cur_sum not in min_heap:
                        heappush(min_heap, cur_sum)
                        if len(min_heap) > 3:
                            heappop(min_heap)
        return sorted(min_heap, reverse=True)