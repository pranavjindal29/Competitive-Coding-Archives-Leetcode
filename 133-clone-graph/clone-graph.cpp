class Solution {
public:
    unordered_map<Node*, Node*> cloned;

    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        if (cloned.count(node)) return cloned[node];

        Node* newNode = new Node(node->val);
        cloned[node] = newNode;

        for (Node* neighbor : node->neighbors) {
            newNode->neighbors.push_back(cloneGraph(neighbor));
        }

        return newNode;
    }
};