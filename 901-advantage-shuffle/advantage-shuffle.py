class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        trace=defaultdict(list)
        n=len(nums2)
        minn1=nums1[:]
        heapq.heapify(minn1)
        minn2=nums2[:]
        heapq.heapify(minn2)
        ref=[]
        while(minn1):
            x=heapq.heappop(minn1)
            #print(x)
            if x<=minn2[0]:
                ref.append(x)
                continue
            #print(x)
            trace[heapq.heappop(minn2)].append(x)
        op=[]
        for i in range(n):
            if trace[nums2[i]]:
                op.append(trace[nums2[i]][0])
                trace[nums2[i]]=trace[nums2[i]][1:]
            else:
                op.append(ref[0])
                ref=ref[1:]
        return op

        

        