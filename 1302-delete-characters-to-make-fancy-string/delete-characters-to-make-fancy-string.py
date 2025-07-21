class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        last = s[0]
        ans.append(last)
        count = 1
        for i in range(1, len(s)):
            if s[i] == last:
                count += 1
                if count < 3:
                    ans.append(s[i])
            else:
                last = s[i]
                count = 1
                ans.append(s[i])
        return "".join(ans)
