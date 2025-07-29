class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 2]
        while fib[-1] <= k:
            fib.append(fib[-1] + fib[-2])
        
        fib.reverse()  
        res = 0
        
        for num in fib:
            if k >= num:
                k -= num
                res += 1
            if k == 0:
                break
        
        return res