class Solution:
    def clumsy(self, n: int) -> int:
        if n==4:
            return 7
        elif n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 6
        if n%4==0:
            return (n+1)
        elif n%4==1:
            return (n+2)
        elif n%4==2:
            return (n+2)
            
        else:
            return (n-1)
    