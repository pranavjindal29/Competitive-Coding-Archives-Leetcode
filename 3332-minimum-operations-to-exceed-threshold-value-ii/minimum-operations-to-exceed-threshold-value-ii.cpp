class Solution {
public:
    static int minOperations(vector<int>& nums, int k) {
        priority_queue<long long, vector<long long>, greater<>> pq(nums.begin(), nums.end());
        int ans=0;
        while(pq.top()<k){
            long long x=pq.top(); pq.pop();
            long long y=pq.top(); pq.pop();
            pq.push(2*x+y);
            ans++;
        }
        return ans;  
    }
};


auto init = []() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();