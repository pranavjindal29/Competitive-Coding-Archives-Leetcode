class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy_count = 0
        yx_count = 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                xy_count += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                yx_count += 1
        if (xy_count + yx_count) % 2 != 0:
            return -1
        swaps = xy_count // 2 + yx_count // 2 
        if xy_count % 2 == 1:  
            swaps += 2
        return swaps