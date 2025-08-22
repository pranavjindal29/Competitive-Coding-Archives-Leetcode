class Solution:
    def bestCoordinate(self, towers, radius):
        def getQuality(x,y):
            total = 0 

            for i,j,q in towers:
                d = math.sqrt((x-i)**2+(y-j)**2)
                if d <= radius:
                    total += math.floor(q/(1+d))

            return total 

        max_val = float("-inf")

        for i in range(51):
            for j in range(51):
                q1 = getQuality(i,j)
                if q1 > max_val:
                    max_val = q1 
                    ans = [i,j]

        return ans 