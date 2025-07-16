class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()

        dictionary = defaultdict(int)
        count = 0
        length = len(nums)

        if len(nums) % k != 0:
            return False

        for num in nums:
            dictionary[num] += 1
        
        for num in nums:
            if dictionary[num] > 0:  
                for curr in range(num, num + k):  
                    if dictionary[curr] == 0:
                        return False  
                    dictionary[curr] -= 1  

        return True
            
            
                    

