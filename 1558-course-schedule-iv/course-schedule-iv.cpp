class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        // Step 1: Initialize the reachability map
        unordered_map<int, unordered_set<int>> reachable;

        // Step 2: Build direct reachability chains
        for (auto& prereq : prerequisites) {
            reachable[prereq[1]].insert(prereq[0]);
        }

        // Step 3: Propagate reachability to account for indirect prerequisites
        for (int i = 0; i < numCourses; ++i) {
            for (int j = 0; j < numCourses; ++j) {
                if (reachable[j].count(i)) {
                    reachable[j].insert(reachable[i].begin(), reachable[i].end());
                }
            }
        }

        // Step 4: Answer the queries
        vector<bool> result;
        for (auto& query : queries) {
            result.push_back(reachable[query[1]].count(query[0]) > 0);
        }
        return result;
    }
};