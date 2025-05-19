class Solution(object):
    def triangleType(self, nums):
        if nums[0] == nums[1] and nums[1] == nums[2]:
            return "equilateral"
        elif (nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]) and \
             nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
            return "isosceles"
        elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2] and \
             nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
            return "scalene"
        return "none"