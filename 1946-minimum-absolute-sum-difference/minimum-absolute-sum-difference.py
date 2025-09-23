class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        arr = sorted(nums1)
        n = len(arr)
        res = maxReduction = 0

        for i, val in enumerate(nums2):
            currDiff = abs(nums1[i] - val)
            res += currDiff
            j = bisect_right(arr, val) - 1
            op1 = abs(val - arr[j])
            op2 = None

            if j + 1 < n:
                op2 = abs(val - arr[j + 1])
            
            maxReduction = max(currDiff - op1, currDiff - op2 if op2 else 0, maxReduction)
    
        return (res - maxReduction) % (10 ** 9 + 7)           