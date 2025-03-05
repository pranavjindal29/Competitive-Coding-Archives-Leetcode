class Solution {
public:
    long long coloredCells(int n) {
        return 1 + 4LL * n * (n - 1) / 2; 
    }
};