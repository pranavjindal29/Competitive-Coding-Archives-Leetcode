class Solution(object):
    def kthFactor(self, n, k):
        count = 0
        for i in range(1,n+1):
            if n % i == 0 :
                count+=1
                if count == k: return i
        return -1
        