class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        n = 3
        rows = [0] * n
        cols = [0] * n
        diag = antidiag = balance = 0
        
        def win(v):
            if v in rows or v in cols or v in [diag, antidiag]: return True
            return False
        
        for i in range(n):
            for j in range(n):
                if board[i][j] != " ":
                    balance += 1 if board[i][j] == "X" else -1
                    rows[i] += 1 if board[i][j] == "X" else -1
                    cols[j] += 1 if board[i][j] == "X" else -1
                    if i == j: diag += 1 if board[i][j] == "X" else -1
                    if i + j == n - 1: antidiag += 1 if board[i][j] == "X" else -1
        
        if not 0 <= balance <= 1: return False
            
        if balance == 0 and win(n): return False
        if balance == 1 and win(-n): return False
        
        return True