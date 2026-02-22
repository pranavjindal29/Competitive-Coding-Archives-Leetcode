class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k == 0: 
            if str(num)[-1] != '0':
                return -1
            else: return 1
        if k > num:
            return -1
        if k == num:
            return 1
        tup = tuple([str(x * k)[-1] for x in range(1, 11)])
        if not str(num)[-1] in tup:
            return -1
        else:
            idx = tup.index(str(num)[-1])

            if num >= k*(idx+1):
                return idx+1
            else:
                return -1