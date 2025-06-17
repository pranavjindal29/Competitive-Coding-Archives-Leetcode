class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num == 2:
                ans.append(-1)
                continue

            num_copy = num
            count = 0

            # Count consecutive 1s from the right
            while num & 1 == 1:
                count += 1
                num >>= 1
            
            # [count]th bit is the position of the last 1, like 100111 (count = 3)
            # Subtract the bit                                     ^
            ans.append(num_copy - 2 ** (count-1))
        
        return ans