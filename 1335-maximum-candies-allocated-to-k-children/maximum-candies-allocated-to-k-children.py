class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:        
        left, right = 1, max(candies)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            children_count = sum(pile // mid for pile in candies)
            
            if children_count >= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return result