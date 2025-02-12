class Solution {
public:
    int maximumSum(vector<int>& nums) {
        int max[82] = {0};
        int ans = -1;
        for (int x : nums) {
            int sum = 0, temp = x;
            while (temp != 0) {
                sum += temp % 10;
                temp /= 10;
            }
            if (max[sum] != 0) ans = std::max(ans, x + max[sum]);
            max[sum] = std::max(max[sum], x);
        }
        return ans;
    }
};