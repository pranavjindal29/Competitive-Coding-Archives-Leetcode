class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l=[]
        for i in range (1, n+1) :
            l.append(str(i))  
        l.sort()  
        for i in range(n):
            l[i]=int(l[i]) 
        return l