from typing import List  

class Solution:  
    def makesquare(self, matchsticks: List[int]) -> bool:  
        total_length = sum(matchsticks)  
        if total_length % 4 != 0:  
            return False  
        side_length = total_length // 4  
        matchsticks.sort(reverse=True)  
        sides = [0] * 4  
        
        def backtrack(index):  
            if index == len(matchsticks):  
                return all(side == side_length for side in sides)  
            for i in range(4):  
                if sides[i] + matchsticks[index] <= side_length:  
                    sides[i] += matchsticks[index]  
                    if backtrack(index + 1):  
                        return True  
                    sides[i] -= matchsticks[index]  
                if sides[i] == 0:  
                    break  
            return False  
        
        return backtrack(0)