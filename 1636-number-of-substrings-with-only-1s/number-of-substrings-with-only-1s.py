class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        count = 0
        for i in s:
            if i == "1":
                count += 1
            else:
                temp = (count*(count+1))//2
                ans += temp
                count = 0
        if count > 0:
            temp = (count*(count+1))//2
            ans += temp
        return ans%(10**9+7)