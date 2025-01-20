class Solution {
public:
    string countAndSay(int n) {
        // Base case: if n is 1, return the initial sequence "1"
        if (n == 1) return "1";
        
        // Start with the first sequence
        string s = "1";

        // Generate the sequence iteratively up to the nth sequence
        for (int i = 2; i <= n; i++) {
            const int len = s.size(); // Length of the current sequence
            string t; 
            t.reserve(len << 1); // Reserve space to minimize reallocations

            // Process the current sequence to build the next one
            for (int j = 0; j < len;) {
                char c = s[j]; // Current character to count
                int count = 1; // Start counting occurrences

                // Count consecutive characters
                while (j + count < len && s[j + count] == c) count++;

                // Append the count and the character to the new sequence
                t.push_back('0' + count); // Convert count to character
                t.push_back(c);

                // Move to the next character group
                j += count;
            }
            // Update the current sequence to the newly generated one
            s = move(t);
        }

        // Return the nth sequence
        return s;
    }
};