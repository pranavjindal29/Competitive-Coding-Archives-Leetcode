
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        temp = copy.deepcopy(board)  #very imp or else use loop to copy

        C = len(board[0])
        R = len(board)
        moves = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for i in range(R):
            for j in range(C):
                neighbors = 0
                for x,y in moves: #above declared valid possible moves              

                    if (0 <= i+x < R) and (0 <= j+y < C):    #check boundaries                    
                        if temp[i+x][j+y] == 1:
                            neighbors += 1
  
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:  #rule 1 and 3
                        board[i][j] = 0
                    if neighbors == 2 or neighbors == 3:  #rule 2
                        board[i][j] = 1

                elif board[i][j] == 0: #rule 4
                    if neighbors == 3:
                        board[i][j] = 1