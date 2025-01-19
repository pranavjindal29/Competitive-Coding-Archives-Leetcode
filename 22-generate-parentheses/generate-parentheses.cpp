class Solution {
public:
    // Helper function to check if the current string is valid.
    bool isValid(string& curr) {
        int count = 0;
        for (char& c : curr) {
            if (c == '(')
                count++;
            else {
                count--;
                if (count < 0) return false;
            }
        }
        return count == 0;
    }

    // Recursive function to generate parentheses.
    void solve(string& curr, int n, vector<string>& ans) {
        if (curr.length() == 2 * n) {
            if (isValid(curr)) {
                ans.push_back(curr);
            }
            return;
        }

        // Add '(' and recurse.
        curr.push_back('(');
        solve(curr, n, ans);
        curr.pop_back();

        // Add ')' and recurse.
        curr.push_back(')');
        solve(curr, n, ans);
        curr.pop_back();
    }

    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string curr = "";
        solve(curr, n, ans);
        return ans;
    }
};