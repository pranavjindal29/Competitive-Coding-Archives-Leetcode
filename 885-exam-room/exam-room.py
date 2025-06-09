class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.pq = [(-n, -1, n)]
        self.nei = {-1: [None, n], n: [-1, None]} # dummy head & tail 

    def seat(self) -> int:
        while self.nei.get(self.pq[0][1], [None]*2)[1] != self.pq[0][2] or self.pq[0][1] != self.nei.get(self.pq[0][2], [None]*2)[0]: heappop(self.pq)
        _, lo, hi = heappop(self.pq)
        if lo == -1: 
            x = 0 
            if hi == self.n: heappush(self.pq, (1-hi, x, hi))
            else: heappush(self.pq, ((x-hi+1)//2, x, hi))
        elif hi == self.n: 
            x = self.n-1
            heappush(self.pq, ((lo-x+1)//2, lo, x))
        else: 
            x = (lo + hi)//2
            heappush(self.pq, ((lo-x+1)//2, lo, x))
            heappush(self.pq, ((x-hi+1)//2, x, hi))
        self.nei[x] = [lo, hi]
        self.nei[lo][1] = self.nei[hi][0] = x
        return x

    def leave(self, p: int) -> None:
        if self.nei[p][0] == -1: 
            heappush(self.pq, (-self.nei[p][1], -1, self.nei[p][1]))
        elif self.nei[p][1] == self.n: 
            heappush(self.pq, (-self.n+1+self.nei[p][0], self.nei[p][0], self.n))
        else: 
            heappush(self.pq, ((self.nei[p][0] - self.nei[p][1] + 1)//2, self.nei[p][0], self.nei[p][1]))
        self.nei[self.nei[p][0]][1] = self.nei[p][1]
        self.nei[self.nei[p][1]][0] = self.nei[p][0]
        self.nei.pop(p)