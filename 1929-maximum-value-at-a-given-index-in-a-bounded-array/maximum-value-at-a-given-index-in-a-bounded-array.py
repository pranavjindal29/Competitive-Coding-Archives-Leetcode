class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        res_i, crr_sum = 0, n
        l, r, w_hill = index + 1, index - 1, 1 
        while crr_sum <= maxSum:
            l -= 1
            r += 1
            if l == index and r == index:
                crr_sum += w_hill
            else:
                l_, r_ = max(l, 0), min(r, n - 1)
                if l < l_ and r > r_:
                    rm = maxSum - crr_sum
                    res_i += int(rm / w_hill) + 1
                    break
                else:
                    w_hill = r_ - l_ + 1
                    crr_sum += w_hill
            res_i += 1
        return res_i