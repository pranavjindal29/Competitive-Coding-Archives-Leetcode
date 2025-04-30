class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(map(int, str(n)))
        k = len(digits)
        if k <=1:
            return -1
        i = k-2

        while i>=0 and digits[i]>= digits[i+1]:
            i -= 1
        print(i)
        if i <0:
            return -1
        
        j = k - 1
        while digits[j] <= digits[i]:
            j-=1
        digits[i], digits[j] = digits[j], digits[i]

        digits[i+1:] = digits[i+1:][::-1]
        result = int(''.join(map(str, digits)))
        return result if result < 2**31 else -1