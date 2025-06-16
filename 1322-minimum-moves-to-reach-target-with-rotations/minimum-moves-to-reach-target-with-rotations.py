class Solution:
    def minimumMoves(self, G: List[List[int]]) -> int:
    	N, S, T, V, c = len(G), [(0, 0, 'h')], [], set(), 0
    	while S:
    		for i in S:
    			if i in V: continue
    			if i == (N-1, N-2, 'h'): return c
    			(a, b, o), _ = i, V.add(i)
	    		if o == 'h':
    				if b + 2 != N and G[a][b+2] == 0: T.append((a, b+1, o))
    				if a + 1 != N and G[a+1][b] == 0 and G[a+1][b+1] == 0: T.append((a+1, b, o)), T.append((a, b, 'v'))
    			elif o == 'v':
    				if a + 2 != N and G[a+2][b] == 0: T.append((a+1, b, o))
    				if b + 1 != N and G[a][b+1] == 0 and G[a+1][b+1] == 0: T.append((a, b+1, o)), T.append((a, b, 'h'))
    		S, T, c = T, [], c + 1
    	return -1
		
		
		
		