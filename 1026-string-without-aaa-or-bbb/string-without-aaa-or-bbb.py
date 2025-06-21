class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a + b > 0:
            if len(res) >= 2 and res[-2:] == ['a', 'a']:
                res.append('b')
                b-=1
            elif len(res) >= 2 and res[-2:] == ['b', 'b']:
                res.append('a')
                a-=1
            elif a > b:
                res.append('a')
                a-=1
            else:
                res.append('b')
                b-=1
            
        return ''.join(res)