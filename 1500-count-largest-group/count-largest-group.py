class Solution:
    def countLargestGroup(self, n: int) -> int:
        s = str(n + 1)
        sm = len(s) * 9 + 1
        dp = [0] * sm
        x = 0
        
        for ch in s:
            digit = int(ch)
            dp2 = [0] * sm
            
            for j in range(sm):
                for k in range(10):
                    if j + k < sm:
                        dp2[j + k] += dp[j]
            
            dp = dp2
            for j in range(digit):
                if x + j < sm:
                    dp[x + j] += 1
            x += digit
        
        dp[0] = 0
        max_freq = max(dp)
        return dp.count(max_freq)