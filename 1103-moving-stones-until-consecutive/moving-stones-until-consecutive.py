class Solution:
    def minMoves(self,a,b,c):
        x=min(a,b,c)
        z=max(a,b,c)
        y=(a+b+c)-(x+z)
        if x+1==y and y+1==z:
            return 0
        if x+1==y or y+1==z:
            return 1
        return min((z-y-1),(y-x-1),2)
        
        
    def maxMoves(self,a,b,c):
        x=min(a,b,c)
        z=max(a,b,c)
        y=(a+b+c)-(x+z)
        return (z-y-1)+(y-x-1)
        
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        return [self.minMoves(a,b,c),self.maxMoves(a,b,c)]