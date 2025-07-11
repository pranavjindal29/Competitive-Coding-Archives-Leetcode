class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        diffs = list(accumulate(s, lambda a,b: a ^ (1 << (ord(b) - 97)), initial = 0))
        return [(diffs[r + 1] ^ diffs[l]).bit_count() // 2 <= k for l,r,k in queries]