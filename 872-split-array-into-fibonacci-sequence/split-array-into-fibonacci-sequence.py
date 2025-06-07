class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n=len(num)


        def f(pos,res,n,fin):
            if pos>=n:
                if len(res)>2:
                    fin.append(res.copy())
                return

            cur=""
            for i in range(pos,n):
                cur+=num[i]

                if cur[0]=="0" and i!=pos:
                    continue 

                if int(cur)>(2**31):
                    break 

                if len(res)>=2:
                    if int(cur)==int(res[-1])+int(res[-2]):
                        res.append(cur)
                        f(i+1,res,n,fin)
                        res.pop()

                else:
                    res.append(cur)
                    f(i+1,res,n,fin)
                    res.pop() 
        fin,res=[],[]
        f(0,res,n,fin)
        ans=[]
        if len(fin)==0 or fin==[]:
            return []
        for i in fin[0]:
            ans.append(int(i))
        return ans
            