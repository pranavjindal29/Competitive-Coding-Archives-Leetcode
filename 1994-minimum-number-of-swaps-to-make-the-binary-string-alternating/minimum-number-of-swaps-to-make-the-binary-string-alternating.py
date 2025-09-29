class Solution:
    def minSwaps(self, s: str) -> int:
        n=len(s)
        import math
        cnti=0
        cnto=0
        flag=True
        if len(s)==1:
            return 0

        for i in range(n):
            p=s[0]
            if i%2==0:
                if s[i]==p:
                    continue
                else:
                    flag=False
                    
            else:
                q=s[1]
                if s[i]==q:

                    continue
                else:
                    flag=False
                   
        if len(set(s))==1:
            return -1

        if flag==True:
            print('u')
            return 0
        for i in range(n):
            if s[i]=="1":
                cnti+=1
        for j in range(n):
            if s[j]=="0":
                cnto+=1
        if abs(cnti-cnto)>1 or len(set(s))==1:
            return -1
       
        mis0=0
        mis1=0
        for i in range(n):
            if i%2==0:
                if s[i] != '0':
                    mis0 += 1
                if s[i] !='1':
                    mis1+= 1
            else:
                if s[i]!='1':
                    mis0 += 1
                if s[i]!= '0':
                    mis1+= 1

        if cnti>cnto:
            return mis1// 2
        elif cnto>cnti:
            return mis0// 2
        else:
            return min(mis0,mis1) // 2
