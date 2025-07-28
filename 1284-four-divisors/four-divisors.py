class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total  = 0 
        for i in nums : 
            cpt = 0   
            current_sum = 0         
            for j in range (1,int(math.sqrt(i))+ 1 ) :    
                if i %  j  == 0  :     
                    if j * j == i :  
                        cpt  +=  1    
                        current_sum += j
                    else :  
                        cpt += 2  
                        current_sum += j   
                        current_sum +=  (i // j)
            if cpt ==  4  :     
                total+= current_sum
        return  total    