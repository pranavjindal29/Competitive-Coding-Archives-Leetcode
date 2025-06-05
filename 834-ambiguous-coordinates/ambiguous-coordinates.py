class Solution:
    def gen_nums(self, s):
        ans = []
        if s == "0" or s[0] != "0":
            ans.append(s)
        
        if s[-1] == '0':
            return ans
        
        if s[0] == '0':
            return ans + ['0.' + s[1:]]

        for i in range(1, len(s)):
            ans.append(s[:i] + '.' + s[i:])
        return ans

    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        res = []
        for left_len in range(1, len(s)):
            l = self.gen_nums(s[:left_len])
            r = self.gen_nums(s[left_len:])
            for n1 in l:
                for n2 in r:
                    res.append(f'({n1}, {n2})')
                    
        return res