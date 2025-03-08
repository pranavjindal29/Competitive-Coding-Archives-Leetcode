class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black_count = 0
        ans = float("inf")
        for i in range(len(blocks)):
            if i - k >= 0 and blocks[i - k] == 'B': 
                black_count -= 1
            if blocks[i] == 'B':
                black_count += 1            
            ans = min(ans, k - black_count)
        
        return ans