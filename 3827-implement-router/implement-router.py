class Router:
    def __init__(self, memoryLimit: int):
        self.maxL = memoryLimit
        self.size = 0
        self.q = deque()
        self.packetCache = defaultdict(int)
        self.entries = defaultdict(deque)
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) not in self.packetCache:
            self.q.append((source,destination,timestamp))
            self.packetCache[(source,destination,timestamp)]+=1
            self.entries[destination].append(timestamp)
            self.size+=1
            if self.size>self.maxL:
                firstPacket = self.q.popleft()
                self.packetCache[firstPacket]-=1
                if self.packetCache[firstPacket]==0:
                    del self.packetCache[firstPacket]
                    self.entries[firstPacket[1]].popleft()
                self.size-=1
            return True
        return False
        
        
    def forwardPacket(self) -> List[int]:
        if self.size>0:
            self.size-=1
            firstPacket= self.q.popleft()
            self.packetCache[firstPacket]-=1
            if self.packetCache[firstPacket]==0:
                del self.packetCache[firstPacket]
                self.entries[firstPacket[1]].popleft()
            return firstPacket
        return []
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = bisect_left(self.entries[destination],startTime)
        right = bisect_right(self.entries[destination],endTime)
        return right-left