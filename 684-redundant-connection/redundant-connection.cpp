class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> graph;

        auto isConnected = [&](int u, int v) {
            unordered_set<int> visited;
            stack<int> stack;
            stack.push(u);

            while (!stack.empty()) {
                int node = stack.top();
                stack.pop();

                if (visited.count(node)) continue;
                visited.insert(node);

                if (node == v) return true;

                for (int neighbor : graph[node]) {
                    stack.push(neighbor);
                }
            }
            return false;
        };

        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];

            if (graph.count(u) && graph.count(v) && isConnected(u, v)) {
                return edge;
            }

            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        return {};
    }
};