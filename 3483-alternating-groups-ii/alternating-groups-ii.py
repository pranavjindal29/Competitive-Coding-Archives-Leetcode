class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:(k-1)])  
        count = 0
        left = 0

        for right in range(len(colors)):
            if right > 0 and colors[right] == colors[right - 1]:
                left = right  
            
            if right - left + 1 >= k:
                count += 1  
        
        return count