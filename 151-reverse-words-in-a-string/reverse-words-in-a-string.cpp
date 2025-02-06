class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word, result;
        vector<string> v;

        while (ss >> word) v.push_back(word);
        reverse(v.begin(), v.end());

        for (int i = 0; i < v.size(); i++) 
            result += (i ? " " : "") + v[i];

        return result;
    }
};