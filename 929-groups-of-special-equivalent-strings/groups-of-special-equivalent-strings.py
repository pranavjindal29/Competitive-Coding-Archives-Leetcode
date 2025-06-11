class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        
        signature = set()
        
        for idx, s in enumerate(A):
            signature.add( ''.join( sorted( s[::2] ) ) + ''.join( sorted( s[1::2] ) )  )
        
        return len( signature )