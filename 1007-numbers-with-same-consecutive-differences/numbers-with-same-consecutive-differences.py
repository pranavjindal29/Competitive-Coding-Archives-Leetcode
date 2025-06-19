class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # edge cases:
        if N == 1:
            return range(10)
        if N == 0:
            return range(1,10)
        
        my_list = [i for i in range(1,10) if i+K<10 or i-K>=0]
    
        # each iteration will increase the length of the numbers in the list:
        for i in range(1,N):
            res = []
            for i in range(len(my_list)):
                if my_list[i] % 10 + K < 10:
                    res.append(my_list[i]*10 + (my_list[i] % 10 + K))
                    
                if 10 > my_list[i] % 10 - K >= 0:
                    res.append(my_list[i] * 10 + (my_list[i] % 10 - K))
                    
            my_list = list(set(res[:]))
            
        # remove duplicates:
        res = list(set(res))
        res.sort()
        return res
    