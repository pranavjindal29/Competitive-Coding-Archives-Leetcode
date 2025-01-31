class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return nullptr;
        Node* leftMost = root;

        while (leftMost->left) {
            Node* currNode = leftMost;

            while (currNode) {
                currNode->left->next = currNode->right;
                if (currNode->next) {
                    currNode->right->next = currNode->next->left;
                }
                currNode = currNode->next;
            }

            leftMost = leftMost->left;
        }

        return root;
    }
};