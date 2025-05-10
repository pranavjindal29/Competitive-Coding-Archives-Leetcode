class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, zero1=sum(nums1), nums1.count(0)
        sum2, zero2=sum(nums2), nums2.count(0)
        if (zero1==0 and sum1<sum2+zero2)or(zero2==0 and sum2<sum1+zero1):
            return -1
        return max(sum1+zero1, sum2+zero2)
        