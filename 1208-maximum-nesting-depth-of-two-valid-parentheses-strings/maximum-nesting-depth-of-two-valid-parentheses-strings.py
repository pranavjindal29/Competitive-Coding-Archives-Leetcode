class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans=[]
        prev=1
        for i in seq:
            if i=='(':
                if prev==0:
                    ans.append(1)
                else:
                    ans.append(0)
            else:
                ans.append(prev)
            if prev==0:
                prev=1
            else:
                prev=0
        return ans