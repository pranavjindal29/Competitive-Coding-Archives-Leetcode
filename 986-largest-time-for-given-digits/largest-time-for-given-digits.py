class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        curMax = -1
        curStr = ""
        for permutation in set(permutations(arr)):
            a, b, c, d = permutation
            hours = a*10 + b
            minutes = c*10 + d
            if hours > 23 or minutes > 59:
                pass
            elif hours*60 + minutes > curMax:
                curMax = hours*60 + minutes
                curStr = str(a) + str(b) + ":" + str(c) + str(d)

        return curStr