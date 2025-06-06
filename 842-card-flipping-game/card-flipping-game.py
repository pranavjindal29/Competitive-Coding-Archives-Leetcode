class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        seen=set()
        doubles=set()
        for f,b in zip(fronts,backs):
            seen.add(f)
            seen.add(b)
            if f==b:
                doubles.add(f)
        return min(seen-doubles,default=0)
        