class Solution {
public:
    void findPaths(TreeNode* root, int targetSum, vector<int>& currentPath, vector<vector<int>>& result) {
        if (!root) return;

        currentPath.push_back(root->val);
        targetSum -= root->val;

        if (!root->left && !root->right && targetSum == 0) {
            result.push_back(currentPath);
        }

        findPaths(root->left, targetSum, currentPath, result);
        findPaths(root->right, targetSum, currentPath, result);

        currentPath.pop_back();
    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> currentPath;
        findPaths(root, targetSum, currentPath, result);
        return result;
    }
};