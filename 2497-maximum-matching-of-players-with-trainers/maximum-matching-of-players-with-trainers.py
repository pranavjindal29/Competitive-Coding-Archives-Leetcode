class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        p.sort()
        t.sort()
        m, match, j=len(t), 0, 0
        for i, pi in enumerate(p):
            while j<m and t[j]<pi: j+=1
            if j<m:
                j+=1
                match+=1
        return match

        