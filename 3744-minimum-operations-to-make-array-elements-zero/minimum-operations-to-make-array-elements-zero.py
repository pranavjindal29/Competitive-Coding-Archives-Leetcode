class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        expSum4=[1]+[0]*17
        def expSum(x):
            if x==0: return 0
            log4=(x.bit_length()-1)>>1
            r=x-(1<<(log4<<1))
            return expSum4[log4]+r*(log4+1)
        for i in range(1,18):
            expSum4[i]=expSum4[i-1]+3*i*(1<<(2*(i-1)))+1
        op=0
        for l1, r in queries:
            op+=(expSum(r)-expSum(l1-1)+1)>>1

        return op