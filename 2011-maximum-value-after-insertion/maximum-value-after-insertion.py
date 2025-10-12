class Solution:
    def maxValue(self, n: str, x: int) -> str:
        neg=False
        x=str(x)
        if n[0]=='-':
            neg=True
            n=n[1:]
        l=len(n)
        if neg:
            for i in range(l):
                if n[i]>x:
                    return '-'+n[:i]+x+n[i:]
            return '-'+n+x
        else:
            for i in range(l):
                if n[i]<x:
                    return n[:i]+x+n[i:]
            return n+x