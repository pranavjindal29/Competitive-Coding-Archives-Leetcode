class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        maxi=[(-values[0],-labels[0])]
        heapq.heapify(maxi)
        for i in range(1,len(values)):
            heapq.heappush(maxi,(-values[i],-labels[i]))
        maps={}
        lim=useLimit
        ans=0
        while numWanted!=0:
            if maxi==[]:
                return ans
            val,lab=heapq.heappop(maxi)
            if -lab in maps and maps[-lab]<lim:
                maps[-lab]+=1
                ans+=(-val)  
                numWanted-=1
            elif -lab not in maps:
                maps[-lab]=1
                ans+=(-val)
                numWanted-=1
        return ans