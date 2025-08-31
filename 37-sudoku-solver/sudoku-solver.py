class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Row, Col, Block=[0]*9, [0]*9, [0]*9
        uncertain=[]
        def set3Cond(i, j, x):
            x2=1<<x
            Row[i]|=x2
            Col[j]|=x2
            Block[(i//3)*3 +j//3]|=x2
        def setup():
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c=='.':
                        uncertain.append((i, j))
                    else:
                        set3Cond(i, j, ord(c)-ord('1'))
        def solve(idx):
            if idx==len(uncertain): return True
            i, j=uncertain[idx]
            bidx=(i//3)*3+j//3
            notMask=~(Row[i]|Col[j]|Block[bidx]) & 0b111111111
            while notMask:
                x=notMask.bit_length()-1
                Bit=1<<x
                board[i][j]=chr(ord('1')+x)
                Row[i]|=Bit
                Col[j]|=Bit
                Block[bidx]|=Bit
                if solve(idx+1): return True
                board[i][j]='.'
                Row[i]^=Bit
                Col[j]^=Bit
                Block[bidx]^=Bit
                notMask^=Bit
            return False
        setup()
        solve(0)
                  