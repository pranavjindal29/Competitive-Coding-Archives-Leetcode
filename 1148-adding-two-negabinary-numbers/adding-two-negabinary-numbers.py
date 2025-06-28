class Solution:
    def addNegabinary(self, arr1, arr2):
        n = (sum(pow(-2, i) for i, v in enumerate(arr1[::-1]) if v) +
             sum(pow(-2, i) for i, v in enumerate(arr2[::-1]) if v))
        res = [] if n else [0]
        while n:
            n, rem = divmod(n, -2)
            if rem < 0:
                n += 1
            res.append(abs(rem))
        res.reverse()
        return res