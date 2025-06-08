class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        r = 1
        n = len(arr)
        main = 0

        if n < 3:
            return 0

        while r < n - 1:
            if arr[r-1] < arr[r] > arr[r+1]:
                l = r - 1

                while l > 0 and arr[l] > arr[l-1]:
                    l -= 1

                while r < n - 1 and arr[r] > arr[r+1]:
                    r += 1

                main = max(main, r - l + 1)
            else:
                r += 1

        return main