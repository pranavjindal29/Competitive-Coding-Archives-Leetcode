class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for n in range(len(arr), 1, -1):
            i = arr.index(n)
            if n == i + 1: continue

            if i != 0:
                res.append(i+1)
            res.append(n) 

            arr[:i+1] = reversed(arr[:i+1])
            arr[:n] = reversed(arr[:n])
        
        return res