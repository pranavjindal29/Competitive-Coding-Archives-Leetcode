class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_diff = 0
        i = 0
        j = 0
        while i<len(nums1) and j <len(nums2):
            if i <= j:
                if nums1[i] <= nums2[j]:
                    max_diff=max(max_diff,j-i)
                    j += 1
                else:
                    i += 1
            else:
                j += 1
        return max_diff
        