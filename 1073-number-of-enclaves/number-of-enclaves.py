class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j):
            if i==-1 or j==-1 or i==n or j==m or grid[i][j]==0:
                return 
            grid[i][j]=0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or n-1==i or m-1==j) and grid[i][j]==1:
                    dfs(i,j)
        s=0
        for i in range(n):
            for j in range(m):
                s+=grid[i][j]
        return s