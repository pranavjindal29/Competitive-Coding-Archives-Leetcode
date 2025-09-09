class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        aware, spread, total = [0] * n, 0, 1
        aware[0] = 1

        for day in range(1, n):
            if day >= delay:
                spread += aware[day - delay]
            if day >= forget:
                forgot = aware[day - forget]
                total -= forgot
                spread -= forgot
            
            aware[day] = spread
            total += spread
        
        return total % (10 ** 9 + 7)