MOD = 10**9 + 7
class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(m,k,i,flag):
            if m<0 or k<0 or m+flag.bit_count() < k: return 0
            if m==0:
                if k==flag.bit_count(): return 1
                else: return 0
            if i>=len(nums): return 0
            res=0
            for c in range(m+1):
                mul=math.comb(m,c)*pow(nums[i], c, MOD)%MOD
                f2 = flag+c
                res += mul*dp(m-c, k-(f2%2), i+1, f2//2)
            return res%MOD
        return dp(M,K,0,0)
        