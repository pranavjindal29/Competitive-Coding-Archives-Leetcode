class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res , i , j = set() , 0 , 0
        while x**i<bound:
            while x**i + y**j <= bound:
                res.add(x**i+y**j)
                j+=1
                if y==1:  break
            i+=1
            j = 0
            if x==1: break
        return list(res)