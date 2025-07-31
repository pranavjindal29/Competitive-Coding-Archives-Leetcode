class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a: int, b: int) -> bool:
            while b!=0:
                a,b=b,a%b
            return a==1
        a=[]
        for i in range(2,n+1,2):
            for j in range(1,i,2):
                if gcd(i,j):
                    a.append(f"{j}/{i}")
        for i in range(3,n+1,2):
            for j in range(1,i):
                if gcd(i,j):
                    a.append(f"{j}/{i}")
        return a