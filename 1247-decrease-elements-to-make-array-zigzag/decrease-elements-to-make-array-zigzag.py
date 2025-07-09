class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return 0
        t1 = t2 = 0
        for i in range(n):
            # for t1
            if(i % 2):
                if(i == n-1):
                    t1 += max(0, nums[i] - nums[i-1] + 1)
                else:
                    t1 += max(0, nums[i] - min(nums[i+1], nums[i-1]) + 1)

            # for t2
            else:
                if(i == 0):
                    t2 += max(0, nums[i] - nums[i+1] + 1)
                elif(i == n-1):
                    t2 += max(0, nums[i] - nums[i-1] + 1)
                else:
                    t2 += max(0, nums[i] - min(nums[i+1], nums[i-1]) + 1)
        return min(t1, t2)