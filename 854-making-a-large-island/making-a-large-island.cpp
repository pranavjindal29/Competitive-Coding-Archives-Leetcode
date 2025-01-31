class Solution {
public:
    int largestIsland(vector<vector<int>>& v) {
        int n = v.size(), idx = 1, ans = 0;
        vector<vector<int>> vis(n, vector<int>(n)), newVis(n, vector<int>(n));
        vector<vector<pair<int, int>>> val(n, vector<pair<int, int>>(n));
        auto dfs = [&](auto &dfs, int i, int j, int &ct) -> void {
            if(i < 0 || j < 0 || i >= n || j >= n || vis[i][j] || !v[i][j]) return;
            vis[i][j] = 1; ct ++;
            dfs(dfs, i + 1, j, ct);
            dfs(dfs, i - 1, j, ct);
            dfs(dfs, i, j + 1, ct);
            dfs(dfs, i, j - 1, ct);
        };
        auto setVal = [&](auto &setVal, int i, int j, int ct) -> void {
            if(i < 0 || j < 0 || i >= n || j >= n || newVis[i][j] || !v[i][j]) return;
            newVis[i][j] = 1; val[i][j] = {idx, ct};
            setVal(setVal, i + 1, j, ct);
            setVal(setVal, i - 1, j, ct);
            setVal(setVal, i, j + 1, ct);
            setVal(setVal, i, j - 1, ct);
        };
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < n; j ++){
                if(vis[i][j]) continue;
                int ct = 0; dfs(dfs, i, j, ct); setVal(setVal, i, j, ct); idx ++; ans = max(ans, ct);
            }
        }
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < n; j ++){
                if(v[i][j]) continue;
                map<int, int> m;
                int top = 0, bottom = 0, left = 0, right = 0;
                if(i - 1 >= 0 && !m[val[i - 1][j].first]) {
                    top = val[i - 1][j].second; m[val[i - 1][j].first]++;
                }
                if(i + 1 < n && !m[val[i + 1][j].first]) {
                    bottom = val[i + 1][j].second; m[val[i + 1][j].first]++;
                }
                if(j - 1 >= 0 && !m[val[i][j - 1].first]) {
                    left = val[i][j - 1].second; m[val[i][j - 1].first]++;
                }
                if(j + 1 < n && !m[val[i][j + 1].first]) {
                    right = val[i][j + 1].second; m[val[i][j + 1].first]++;
                }
                ans = max(ans, top + bottom + left + right + 1);
            }
        }
        return ans;
    }
};