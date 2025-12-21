class Solution: 
    def minDeletionSize(self, strs: List[str]) -> int:

        tpse, n, m = zip(*strs), len(strs), len(strs[0])
        strs = [''] * n

        for nxt in tpse:
            temp = [strs[i]+nxt[i] for i in range(n)]
            if temp == sorted(temp): strs = temp
            
        return m - len(strs[0])