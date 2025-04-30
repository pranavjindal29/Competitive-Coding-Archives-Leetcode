class Solution:
    def subarraySum(self, nums, k):
        from collections import defaultdict
        
        map = defaultdict(int)
        map[0] = 1
        sum = 0
        count = 0
        
        for num in nums:
            sum += num
            if (sum - k) in map:
                count += map[sum - k]
            map[sum] += 1
        
        return count