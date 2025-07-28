class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        C=0
        F=[]
        E=[i for i in range(lo,hi+1)]
        for i in range(lo,hi+1):
            C=0
            while(i>1):
                if i%2==0:
                    i//=2
                else:
                    i=3*i+1
                C+=1
            F.append(C)
        return [x for _, x in sorted(zip(F,E))][k-1]
