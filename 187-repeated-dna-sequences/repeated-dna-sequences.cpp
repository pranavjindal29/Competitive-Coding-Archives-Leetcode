class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string,int> mp;
        int i=0,j=0;
        vector<string> res;
        string temp="";
        while(i<s.size()){
               
            if(i-j==9){
                temp=s.substr(j,i-j+1);j++;
                if(mp.find(temp)==mp.end()){
                    mp[temp]=1;
                }
                else{
                    if(mp[temp]==1){res.push_back(temp);}
                    mp[temp]++;
                }

            }
i++;
        }
     return res;
    }
};