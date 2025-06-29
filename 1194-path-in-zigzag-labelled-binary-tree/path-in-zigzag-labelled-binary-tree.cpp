class Solution {
private:
    int getDepth(int a){
        return log2(a)+1;
    }
    int getOpp(int a,int dep){
        return (1<<(dep))-1-(a-(1<<(dep-1)));
    }
public:
    vector<int> pathInZigZagTree(int label) {
        vector<int>ans;
        int depth=getDepth(label);
        while(label!=1){
            ans.push_back(label);
            if(depth%2==0){
                 label=getOpp(label,depth);
            }
            label/=2;
            if(depth&1){
                label=getOpp(label,depth-1);
            }
            depth--;
        }
        ans.push_back(1);
        reverse(begin(ans),end(ans));
        return ans;
    }
};