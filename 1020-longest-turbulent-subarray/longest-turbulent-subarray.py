class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        down = up = res = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                down = up + 1
                up = 1
            elif arr[i] < arr[i - 1]:
                up = down + 1
                down = 1
            else:
                down = 1
                up = 1
            res = max(res, up, down)
        return res