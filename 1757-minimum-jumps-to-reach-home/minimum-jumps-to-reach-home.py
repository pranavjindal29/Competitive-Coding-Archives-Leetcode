class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0

        max_x = 3 * (x + a + b)
        forbidden = set(forbidden)
        q1 = [0]
        q2 = []
        q3 = []
        level = 0
            
        while len(q1) > 0 or len(q2) > 0:
            for i in q1:
                if i in forbidden or i > max_x:
                    continue
                    
                if i == x:
                    return level

                forbidden.add(i)

                npos = i + a
                if npos not in forbidden:
                    q2.append(npos)
                    npos = npos - b
                    if npos not in forbidden and npos > 0:
                        q3.append(npos)
                    
            q1 = q2
            q2 = q3
            q3 = []
            level += 1
    
        return -1