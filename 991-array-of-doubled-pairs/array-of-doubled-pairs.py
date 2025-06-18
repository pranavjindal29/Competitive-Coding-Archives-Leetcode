class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        if sum(arr)%3 != 0: return False
        
        expected = defaultdict(int)
        for a in sorted(arr, key = abs):
            if expected[a] > 0:
                expected[a] -= 1
            else:
                expected[2*a] += 1
        
        return all(x == 0 for x in expected.values())