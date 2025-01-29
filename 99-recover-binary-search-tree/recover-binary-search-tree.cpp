class Solution {
public:
    TreeNode* first = nullptr;
    TreeNode* second = nullptr;
    TreeNode* prev = nullptr;

    void recoverTree(TreeNode* root) {
        inorderTraversal(root);
        swap(first->val, second->val);
    }

    void inorderTraversal(TreeNode* root) {
        if (!root) return;
        
        inorderTraversal(root->left);

        if (prev && root->val < prev->val) {
            if (!first) first = prev;
            second = root;
        }
        prev = root;

        inorderTraversal(root->right);
    }
};