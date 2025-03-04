class Solution {
public:
    TreeNode* reverseOddLevels(TreeNode* root) {
        DFS(root->left, root->right, 0);
        return root;
    }

private:
    void DFS(TreeNode* leftChild, TreeNode* rightChild, int level) {
        if (leftChild == nullptr || rightChild == nullptr) {
            return;
        }
        if (level % 2 == 0) {
            int temp = leftChild->val;
            leftChild->val = rightChild->val;
            rightChild->val = temp;
        }
        DFS(leftChild->left, rightChild->right, level + 1);
        DFS(leftChild->right, rightChild->left, level + 1);
    }
};