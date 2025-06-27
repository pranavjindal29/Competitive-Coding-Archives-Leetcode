class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq_map = collections.defaultdict(int)
        maxFreq = 0
        for code in barcodes:
            freq_map[code] += 1
            if freq_map[code] > freq_map[maxFreq]:
                maxFreq = code
        
        n = len(barcodes)
        idx = 0
        res = [0]*n
        idx = 0
        for v in range(freq_map[maxFreq]):
            res[idx] = maxFreq
            idx += 2
        
        del freq_map[maxFreq]
        for k,v in freq_map.items():
            for _ in range(v):
                if idx >= n:
                    idx = 1
                res[idx] = k
                idx += 2
                
        return res