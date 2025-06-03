class Solution:
    def numSubarrayBoundedMax(self, a: List[int], l: int, r: int) -> int:
        return sum(sum(accumulate(enumerate(g),lambda q,p:(q,p[0]+1)[l<=p[1]<=r],initial=0))
            for _,g in groupby(a,r.__ge__) if _)