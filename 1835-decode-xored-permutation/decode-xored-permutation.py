class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        first = 0
        n = len(encoded) + 1
        for i in range(1,n+1):
            first = first ^ i

        for i in range(1,n,2):
            first = first ^ encoded[i]
            
        
        perm = [0] * n
        perm[0] = first
        for i in range(n-1):
            perm[i+1] = perm[i] ^ encoded[i]
        return perm