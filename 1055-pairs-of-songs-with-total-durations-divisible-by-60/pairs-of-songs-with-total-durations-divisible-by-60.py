class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        HashMap = {}
        pairs = 0
        
        for t in time:
            numMod = t % 60
            
            if numMod == 0:
                if 0 in HashMap:
                    pairs += HashMap[0]
            elif (60 - numMod) in HashMap:
                pairs += HashMap[60 - numMod]
                
            if numMod in HashMap:
                HashMap[numMod] += 1
            else:
                HashMap[numMod] = 1
                
        return pairs
                