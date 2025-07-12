class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if (k == 1):
            return self.ConcatenationMaxSum(arr) % (10**9 + 7)
        
        sum_ = sum(arr)
        arr2_ans = self.ConcatenationMaxSum(arr * 2) % (10**9 + 7)
        if sum_ > 0:
            return (arr2_ans + (sum_ * (k-2))) % (10**9 + 7)
        else :
            return arr2_ans
    
    def ConcatenationMaxSum(self, arr: List[int]) -> int:#sum, start, end
        s, s_tmp = 0, 0
        phase = True
        for i, x in enumerate(arr):
            s_tmp += x
            if (s_tmp < 0):
                s_tmp = 0
            
            if (phase):
                if (x >= 0):
                    s += x
                else:
                    phase = False
                    
            elif (s_tmp > s):
                s = s_tmp
                phase = True
        
        return s