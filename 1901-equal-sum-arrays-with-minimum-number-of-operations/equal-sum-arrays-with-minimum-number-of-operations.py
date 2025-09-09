class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 < s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        diff = s1 - s2
        cnt = [0] * 6
        for x in nums1:
            if x > 1:
                cnt[x - 1] += 1
        for x in nums2:
            if x < 6:
                cnt[6 - x] += 1
        ops = 0
        for d in range(5, 0, -1):
            if diff <= 0:
                break
            take = min(cnt[d], (diff + d - 1) // d)
            ops += take
            diff -= take * d
        return ops if diff <= 0 else -1