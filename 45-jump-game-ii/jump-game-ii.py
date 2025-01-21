class Solution:
    def jump(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        counter = 0
        while p1 + nums[p1] < len(nums) - 1:
            p2 = p1 + 1
            for i in range(p1+2, p1 + nums[p1] + 1):
                if nums[i] +i > nums[p2] + p2:
                    p2 = i
            p1 = p2
            counter+=1
        if p1 >= len(nums) - 1:
            return counter
        else:
             return counter +1