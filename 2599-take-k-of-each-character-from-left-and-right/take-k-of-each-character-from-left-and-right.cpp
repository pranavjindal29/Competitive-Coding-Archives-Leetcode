class Solution {
public:
    int takeCharacters(string s, int k) {
        int n = s.size();
        int l = 0, r = 0, m;
        int ans = n; 
        int a = 0, b = 0, c = 0;

        // Count total occurrences of 'a', 'b', and 'c'
        int totalA = 0, totalB = 0, totalC = 0;
        for (char ch : s) {
            if (ch == 'a') totalA++;
            else if (ch == 'b') totalB++;
            else if (ch == 'c') totalC++;
        }

        // If there are not enough 'a', 'b', or 'c', return -1
        if (totalA < k || totalB < k || totalC < k) {
            return -1;
        }

        // Reset counters and start sliding window
        a = 0, b = 0, c = 0;
        while (r < n) {
            if (s[r] == 'a') a++;
            if (s[r] == 'b') b++;
            if (s[r] == 'c') c++;
            r++;

            // Shrink window if it exceeds the limits
            while (a > totalA - k || b > totalB - k || c > totalC - k) {
                if (s[l] == 'a') a--;
                if (s[l] == 'b') b--;
                if (s[l] == 'c') c--;
                l++;
            }

            // Update the answer with the minimum number of characters to remove
            ans = min(ans, n - (r - l));
        }

        return ans;
    }
};