class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0  

        for num in range(low, high + 1):
            s = str(num)  
            n = len(s)

            if n % 2 != 0:
                continue  

            half = n // 2
            left = sum(int(s[i]) for i in range(half))
            right = sum(int(s[i]) for i in range(half, n))

            if left == right:
                count += 1

        return count