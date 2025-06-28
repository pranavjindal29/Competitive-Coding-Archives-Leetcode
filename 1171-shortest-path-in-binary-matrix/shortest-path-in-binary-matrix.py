class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        vis=[[0]*n for _ in range(m)]
        if grid[0][0]==1:
            return -1
        queue=[(0,0,1)]
        vis[0][0]=1
        while queue:
            x,y,d=queue.pop(0)
            if x==m-1 and y==n-1:
                return d

            for i in range(-1,2):
                for j in range(-1,2):
                    if 0<=x+i<m and 0<=y+j<n:
                        if vis[x+i][y+j]==0 and grid[x+i][y+j]==0:
                            queue.append((x+i,y+j,d+1))
                            vis[x+i][y+j]=1
        return -1

        