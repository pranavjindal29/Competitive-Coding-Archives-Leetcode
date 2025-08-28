class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        d = {}
        for i in range(n):
            low_tri_col = 0
            low_tri_row = i
            li = []
            ind = (low_tri_row,low_tri_col)
            while low_tri_row<n and low_tri_col<m:
                li.append(grid[low_tri_row][low_tri_col])
                low_tri_row+=1
                low_tri_col+=1
            li.sort()
            li = li[::-1]
            d[ind] = li
        
        for i in range(1,m):
            upp_tri_col = i
            upp_tri_row = 0
            li = []
            ind = (upp_tri_row,upp_tri_col)
            while upp_tri_row<n and upp_tri_col<m:
                li.append(grid[upp_tri_row][upp_tri_col])
                upp_tri_row+=1
                upp_tri_col+=1
            li.sort()
            d[ind] = li
        
        ans = [[0] * m for _ in range(n)]


        for i in d:
            r,c = i
            li = d[i]
            ind = 0
            while r<n and c<m:
                ans[r][c] = li[ind]
                r+=1
                c+=1
                ind+=1 

        return ans