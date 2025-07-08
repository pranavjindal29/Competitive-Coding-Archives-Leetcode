class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        curr = [0, 0]
        res = ""
        for letter in target:
            ind = ord(letter) - ord('a')
            next_pos = [ind//5, ind % 5]
            while curr != next_pos:
                while curr[1] != next_pos[1]:
                    if curr[1] < next_pos[1]:
                        if curr[0] == 5:
                            break
                        res += "R"
                        curr[1]+=1
                    elif curr[1] > next_pos[1]:
                        res += "L"
                        curr[1]-=1
                    
                while curr[0] != next_pos[0]:
                    if curr[0] < next_pos[0]:
                        if curr[0] == 4 and curr[1] != 0:
                            break
                        res += "D"
                        curr[0]+=1
                    elif curr[0] > next_pos[0]:
                        res += "U"
                        curr[0]-=1
                    
            if curr == next_pos:
                res += "!"
                
        return res