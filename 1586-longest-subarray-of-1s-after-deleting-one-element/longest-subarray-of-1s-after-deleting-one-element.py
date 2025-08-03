class Solution:
    def longestSubarray(self, nums) -> int:
        if 0 not in nums:
            return len(nums)-1
        maximum=0
        previous=0
        current=0
        for num in nums:
            if num==1:
                current+=1
                if current+previous>maximum:
                    maximum=current+previous
            else:
                previous=current
                current=0
        return maximum