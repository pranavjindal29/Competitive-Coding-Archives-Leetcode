class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque() 
        dire = deque()

        for i, v in enumerate(senate):
            if v == "R": 
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            r_index = radiant.popleft() 
            d_index = dire.popleft()

            if r_index < d_index: 
                radiant.append(r_index + len(senate))
            else:
                dire.append(d_index + len(senate))
        
        return "Radiant" if radiant else "Dire"