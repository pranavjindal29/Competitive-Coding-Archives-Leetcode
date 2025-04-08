class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)

        def is_distinct():
            return all(v <= 1 for v in freq.values())

        if is_distinct():
            return 0

        k = 0
        while nums:
            if len(nums) < 3:
                return k + 1

            for i in range(3):
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
            nums = nums[3:]
            k += 1
            if is_distinct():
                return k

        return k