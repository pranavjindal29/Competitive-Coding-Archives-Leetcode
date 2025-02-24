class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ls = []
        flag = False

        def backtrack(index):
            nonlocal flag
            if index == len(num):
                if len(ls) < 3:
                    return
                # Check additive property for the complete sequence
                for i in range(2, len(ls)):
                    if ls[i] != ls[i-1] + ls[i-2]:
                        return
                flag = True
                return

            for i in range(index, len(num)):
                # Skip numbers with leading zeros
                if num[index] == '0' and i > index:
                    break
                curr = int(num[index:i+1])
                # If we have at least two numbers, check if the current number fits
                if len(ls) >= 2 and curr != ls[-1] + ls[-2]:
                    continue
                ls.append(curr)
                backtrack(i+1)
                ls.pop()

        backtrack(0)
        return flag