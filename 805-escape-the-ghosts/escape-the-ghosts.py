class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        human = (abs(target[0])+abs(target[1]))
        
        minghosts = float("inf")
        for x,y in ghosts:
            minghosts = min(minghosts,abs(x-target[0])+abs(y-target[1]))
        
        return human<minghosts