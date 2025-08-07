class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        ROW=len(fruits)
        total=0
        for i in range(ROW):
            total+=fruits[i][i]

        @cache
        def walk(down,step,r,c):
            #cut path
            if r<0 or c<0 or r>=ROW or c>=ROW or (down and c<=r) or (not down and r<=c):
                return -float("inf")

            if step==0 :
                    return fruits[r][c]

            if down:
                s1=walk(down,step-1,r+1,c-1)
                s2=walk(down,step-1,r+1,c)
                s3=walk(down,step-1,r+1,c+1)
                return max([s1,s2,s3])+fruits[r][c]
            else:
                s1=walk(down,step-1,r-1,c+1)
                s2=walk(down,step-1,r,c+1)
                s3=walk(down,step-1,r+1,c+1)
                return max([s1,s2,s3])+fruits[r][c]

        total+=walk(True,ROW-2,0,ROW-1)
        total+=walk(False,ROW-2,ROW-1,0)

        return total