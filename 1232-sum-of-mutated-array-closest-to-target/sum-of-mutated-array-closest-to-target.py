class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        def score(value, target, p):
            s = 0
            for element in p:
                if (element>=value):
                    s += value
                else:
                    s += element
            return abs(s-target)

        p = sorted(arr)
        
        l, r = 0, target
        while (l < r):
            m1 = l + ((r-l)//3)
            m2 = l + ((2+2*(r-l))//3)
            score1 = score(m1, target, p)
            score2 = score(m2, target, p)
            if (score1 <= score2):
                r = m2-1
            else:
                # if score1 > scor2
                l = m1+1
        print(score(l, target, p))
        return l
        

