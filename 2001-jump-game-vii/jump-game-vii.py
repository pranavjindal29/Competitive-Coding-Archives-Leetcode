from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q = deque([0])
        for i in range(1, n):
            if s[i] != '0':
                continue
            
            while q and q[0] + maxJump < i:
                q.popleft()
            
            if q and q[0] + minJump <= i:
                q.append(i)
        
        return (len(q) > 0 and q[-1] == n-1)