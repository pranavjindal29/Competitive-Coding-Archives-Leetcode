class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.live_tokens = {}
        self.timeline = deque()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.live_tokens[tokenId] = 1
        self.timeline.append((currentTime, tokenId))
    
    def _prune(self, currentTime):
        while self.timeline and self.timeline[0][0] <= (currentTime - self.ttl):
            _, token = self.timeline.popleft()
            self.live_tokens[token] -= 1
            if self.live_tokens[token] == 0:
                del self.live_tokens[token]

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._prune(currentTime)
        if tokenId in self.live_tokens:
            self.live_tokens[tokenId] += 1
            self.timeline.append((currentTime, tokenId))        
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._prune(currentTime)
        return len(self.live_tokens)