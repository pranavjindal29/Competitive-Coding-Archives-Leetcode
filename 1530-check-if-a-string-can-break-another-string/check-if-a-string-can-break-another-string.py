class Solution:
    def checkIfCanBreak(self, *q) -> bool:
        return all(map(le,*sorted(map(sorted,q))))