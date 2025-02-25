class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        temp.sort(reverse=True)
        for i in range(1,len(nums),2):
            nums[i] = temp.pop(0)
        for i in range(0,len(nums),2):
            nums[i] = temp.pop(0)
        return