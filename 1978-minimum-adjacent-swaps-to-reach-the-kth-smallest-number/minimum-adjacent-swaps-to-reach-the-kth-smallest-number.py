class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        s = list(num)
        n = len(s)
        def perm(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i+1]:
                i -= 1
            if i < 0:
                return
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i+1:] = reversed(arr[i+1:])
    
        for _ in range(k):
            perm(s)

        comp = list(num)
        cnt = 0
        for i in range(n):
            if s[i] != comp[i]:
                j = i+1
                while s[j] != comp[i]:
                    j += 1
                while j > i:
                    s[j], s[j-1] = s[j-1], s[j]
                    j -= 1
                    cnt += 1
        return cnt