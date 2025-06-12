class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.lst=encoding

    def next(self, n: int) -> int:
        num=-1
        while self.lst and n>0:
            if n<=self.lst[0]:
                self.lst[0]-=n  
                n=0
                num=self.lst[1]
            else:
                n-=self.lst[0]
                self.lst[0]=0
            if self.lst[0]==0:
                self.lst.pop(0)
                self.lst.pop(0)
        if n>0:
            return -1
        return num