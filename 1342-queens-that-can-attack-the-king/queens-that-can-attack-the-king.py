class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        queens = set(map(tuple,queens))
        choices = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
        for dx,dy in choices:
            x,y = king
            nx = x+dx
            ny = y+dy
            while 0<=nx<8 and 0<=ny<8:
                if (nx,ny) in queens:
                    ans.append([nx,ny])
                    break
                nx +=dx
                ny +=dy
        return ans