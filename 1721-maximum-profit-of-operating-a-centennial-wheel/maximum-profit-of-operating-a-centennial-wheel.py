class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit_time = -1
        peak_profit = 0
        current_profit = 0
        people_waiting = 0
        time = 0
        
        while time < len(customers) or people_waiting > 0:
            if time < len(customers):
                people_waiting += customers[time]
            
            boarded = min(4, people_waiting)
            people_waiting -= boarded
            current_profit += boarded * boardingCost - runningCost
            
            if current_profit > peak_profit:
                max_profit_time = time + 1
                peak_profit = current_profit
            
            time += 1
        
        return max_profit_time