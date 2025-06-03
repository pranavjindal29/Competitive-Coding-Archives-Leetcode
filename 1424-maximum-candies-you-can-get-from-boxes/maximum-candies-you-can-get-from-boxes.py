from collections import deque
class Solution:
    def maxCandies(self, stat, choco, keys, containedBoxes, curBoxes):
        dq = deque()
        
        for box_ind in curBoxes:
            for key in keys[box_ind]:
                stat[key] = 1

            if stat[box_ind] == 0:
                dq.append(box_ind)
            else:
                dq.appendleft(box_ind)
        
        ans = 0
        
        while dq:
            ind = dq.popleft()

            if stat[ind] == 0:
                break
            elif stat[ind] == 1:
                ans += choco[ind]
                for key in keys[ind]:
                    stat[key] = 1

            for new_box_ind in containedBoxes[ind]:
                if stat[new_box_ind] == 0:
                    dq.append(new_box_ind)
                else:
                    dq.appendleft(new_box_ind)

        return ans