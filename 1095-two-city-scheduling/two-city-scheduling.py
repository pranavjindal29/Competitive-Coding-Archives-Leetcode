class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        n = len(costs)
        spaceA, spaceB = n//2, n//2
        priority = sorted(costs, reverse = True, key = lambda x: abs(x[0] - x[1]))
        
        price = 0
        for pair in priority:
            city = pair.index(min(pair))
            if city == 0:
                if spaceA > 0:
                    price += pair[0]
                    spaceA -= 1
                else:
                    price += pair[1]
                    spaceB -= 1
            else:
                if spaceB > 0:
                    price += pair[1]
                    spaceB -= 1
                else:
                    price += pair[0]
                    spaceA -= 1
        
        return price