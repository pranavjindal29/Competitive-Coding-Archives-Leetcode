from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_num = max(costs)
        count = [0] * (max_num + 1)
        
        for cost in costs:
            count[cost] += 1
        
        index = 0
        sorted_costs = []
        for i in range(len(count)):
            sorted_costs.extend([i] * count[i])
        
        for i, cost in enumerate(sorted_costs):
            coins -= cost
            if coins == 0:
                return i + 1
            if coins < 0:
                return i
        return len(costs) if coins > 0 else 0