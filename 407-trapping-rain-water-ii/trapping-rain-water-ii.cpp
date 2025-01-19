#define pii pair<int, int>
#define piii pair<int, pii>
#define f first
#define s second

class Solution {
public:
    int m,n;
    bool isValid(int x, int y){
        return min(x,y) >= 0 && x < m && y < n;
    }

    int trapRainWater(vector<vector<int>>& matrix) {
        m = matrix.size();
        n = matrix[0].size();

        vector<vector<bool>> visited(m+1, vector<bool>(n+1, false));
        priority_queue<piii, vector<piii>, greater<piii>> pq;
        int dx[4] = {1, -1, 0, 0};
        int dy[4] = {0, 0, 1, -1};

        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (i == 0 || i == m-1 || j == 0 || j == n-1){
                    pq.push({matrix[i][j], {i, j}});
                }
            }
        }

        int ans = 0;
        while(!pq.empty()){
            int i = pq.top().s.f;
            int j = pq.top().s.s;
            int h = pq.top().f;
            pq.pop();

            if (visited[i][j]) continue;
            visited[i][j] = 1;
            ans += h - matrix[i][j];

            for (int k = 0; k < 4; k++){
                int nx = i + dx[k];
                int ny = j + dy[k];
                if (isValid(nx, ny) && !visited[nx][ny]){
                    pq.push({max(h, matrix[nx][ny]), {nx, ny}});
                }
            }
        }

        return ans;
    }
};