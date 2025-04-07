class Solution:
    def magicalString(self, n: int) -> int:
        # Base magical string
        ms = [1, 2, 2]
        
        if n <= len(ms):
            return ms[:n].count(1)
        
        pointer = 2  # Pointer starts at the third element
        current = 1  # Start adding `1`s
        
        # Dynamically extend the magical string
        while len(ms) < n:
            ms.extend([current] * ms[pointer])
            pointer += 1
            current = 3 - current  # Alternate between 1 and 2
        
        return ms[:n].count(1)