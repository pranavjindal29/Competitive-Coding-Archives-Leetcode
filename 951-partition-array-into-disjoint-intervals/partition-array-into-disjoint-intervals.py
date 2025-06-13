class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        min_ = A.index(min(A))
        if min_ == 0:
            return 1
        
        max_before_min = A.index(max(A[:min_]))
        while len(A[min_+1:])>0 and min(A[min_+1:]) < A[max_before_min]:
            min_ = len(A) - A[::-1].index( min(A[min_+1:])) - 1
            max_before_min = A.index(max(A[:min_]))

        i = len(A)-1
        while i >= max_before_min and A[i] >= A[max_before_min]:
            i-=1
        
        return i+1