class Solution:
    def maxDiff(self, num: int) -> int:
        s_num=str(num)
        a=s_num
        for digit in s_num:
            if digit!='9':
                a=s_num.replace(digit,'9')
                break
        b=s_num
        if s_num[0]!='1':
            b=s_num.replace(s_num[0],'1')
        else:
            for digit in s_num[1:]:
                if digit not in '01':
                    b=s_num.replace(digit,'0')
                    break
        return int(a)-int(b)