class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int r[9]{}, c[9]{}, b[9]{};
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j]=='.') continue;
                int d=board[i][j]-'1',m=1<<d,k=(i/3)*3+j/3;
                if(r[i]&m||c[j]&m||b[k]&m) return false;
                r[i]|=m; c[j]|=m; b[k]|=m;
            }
        }
        return true;
    }
};