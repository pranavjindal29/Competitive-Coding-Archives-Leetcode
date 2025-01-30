class Solution {
    void dfs(TreeNode* h, ListNode* &head) {
        if (!h) return;
        dfs(h->left, head);
        h->val = head->val;
        head = head->next;
        dfs(h->right, head);
    }

public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (head == nullptr) return nullptr;

        // Step 1: Count the number of nodes
        int n = 0;
        ListNode* temp = head;
        while (temp) {
            n++;
            temp = temp->next;
        }

        // Step 2: Create an empty tree with the required structure
        TreeNode* root = new TreeNode();
        queue<TreeNode*> q;
        q.push(root);
        n--;

        while (n > 0) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (n > 0) {
                    node->left = new TreeNode();
                    q.push(node->left);
                    n--;
                }
                if (n > 0) {
                    node->right = new TreeNode();
                    q.push(node->right);
                    n--;
                }
            }
        }

        // Step 3: Assign values to the tree nodes
        dfs(root, head);

        return root;
    }
};