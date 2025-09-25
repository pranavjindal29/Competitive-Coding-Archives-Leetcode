class Solution:
    def maxSumMinProduct(self, nums):
        MOD = int(1e9 + 7)
        stack = deque()
        max_sum = float("-inf")
        prefix_sum = list(accumulate(nums))
        nums.append(float("-inf"))

        for i in range(len(nums)):
            curr = nums[i]
            while stack and nums[stack[-1]] >= curr:
                popped_idx = stack.pop()
                curr_sum = prefix_sum[i - 1] - \
                    (0 if not stack else prefix_sum[stack[-1]])
                max_sum = max(max_sum, curr_sum * nums[popped_idx])
            stack.append(i)
        return max_sum % MOD