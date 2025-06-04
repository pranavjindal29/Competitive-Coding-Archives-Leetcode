class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        f = lambda x: (tuple(zip(*[(k, len(tuple(g)))
                       for k,g in groupby(x)])))
       
        (sCh, sCt), ans = f(s), 0

        for word in words:
            wCh, wCt = f(word)

            if sCh == wCh:
                for sc, wc in zip(sCt, wCt):
                    
                    if sc < wc or (sc < 3 and sc != wc): break

                else: ans+= 1 

        return ans