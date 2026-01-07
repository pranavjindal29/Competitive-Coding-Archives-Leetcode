
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        ROWS = k+1
        COLS = len(nums)

        PS = [0] * COLS
        PS[0] = nums[0]

        for i in range(1, COLS):
            PS[i] = PS[i-1] + nums[i]


        DP = []
        for _ in range(ROWS):
            DP.append([0] * COLS)

        #Fill out the first row in DP.

        max_ = nums[0]
        for i in range(1, COLS):
            max_ = max(max_, nums[i])

            DP[0][i] = max_ * (i + 1) - (PS[i])
        

        for r in range(1, ROWS):
            for c in range(1, COLS):
                DP[r][c] = DP[r-1][c]

                right_max = nums[c]
                right_sum = 0

                for x in range(c, 0, -1):
                    right_max = max(right_max, nums[x])
                    right_sum += nums[x]
                    right_length = c - x + 1

                    


                    DP[r][c] = min(
                        DP[r][c],
                        DP[r-1][x-1] + (right_max * right_length) - right_sum
                    )

        
        return DP[-1][-1]