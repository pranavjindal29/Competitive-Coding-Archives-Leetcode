class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
        int n=nums.size();
        vector<int> prefix(n,0);
        prefix[0]=nums[0];
        for(int i=1;i<n;i++)
        {
            prefix[i]=prefix[i-1]+nums[i];
        }
        vector<pair<int,int>> prev_best(n,{0,0});
        int sum=0;
        for(int i=0;i<k;i++)
        {
            sum+=nums[i];
        }
        prev_best[k-1]={sum,0};
        for(int i=k;i<n;i++)
        {
            sum-=nums[i-k];
            sum+=nums[i];
            if(sum>prev_best[i-1].first)
            {
                prev_best[i]={sum,i-(k-1)};
            }
            else{
                prev_best[i]=prev_best[i-1];
            }
        }
        vector<pair<int,int>> next_best(n,{0,0});
        sum=0;
        for(int i=n-1;i>=n-k;i--)
        {
            sum+=nums[i];
        }
        next_best[n-k]={sum,n-k};
        for(int i=n-k-1;i>=0;i--)
        {
            sum-=nums[i+k];
            sum+=nums[i];
            if(sum>=next_best[i+1].first)
            {
                next_best[i]={sum,i};
            }
            else{
                next_best[i]=next_best[i+1];
            }
        }
        int ans=0;
        vector<int> state={-1,-1,-1};
        for(int i=k;i<=n-k*2;i++)
        {
            int x=prev_best[i-1].first+prefix[i+k-1]-prefix[i-1]+next_best[i+k].first;
            if(x>ans)
            {
                ans=x;
                state={prev_best[i-1].second,i,next_best[i+k].second};
            }
        }
        return state;
    }
};