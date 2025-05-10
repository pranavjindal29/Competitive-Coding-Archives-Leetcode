class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        return self.dp(price, special, needs, {})

    def dp(self, prices, specials, needs, memo):

        if tuple(needs) in memo:
            return memo[tuple(needs)]
        
        '''
        return minimum success path, choosing between the price or special
        '''

        cost = sum(prices[i] * needs[i] for i in range(len(prices)))

        for offer in specials:
            # consider the special offer
            updated_needs = [needs[j] - offer[j] for j in range(len(needs))]

            if all(updated_needs[j] >= 0 for j in range(len(needs))):
                # total cost or pay for the special
                cost = min(cost, offer[-1] + self.dp(prices, specials, updated_needs, memo))

        memo[tuple(needs)] = cost
        return cost