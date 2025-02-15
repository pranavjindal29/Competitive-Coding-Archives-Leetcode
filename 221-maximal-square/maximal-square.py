class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        
        @lru_cache(None)
        def helper(row,col):
            if not 0<=row<rowLen or not 0<=col<colLen or grid[row][col]=='0':
                return 0
            
            goRight = helper(row,col+1)
            goDown = helper(row+1,col)
            goDiag = helper(row+1,col+1)
            # 1*1 tile is always a grid, thus we add one
            return 1 + min(goRight,goDown,goDiag)
        lenOfLongestSide = 0
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j]=='1':
                    lenOfLongestSide = max(lenOfLongestSide,helper(i,j))
        area = lenOfLongestSide**2
        return area
        

            