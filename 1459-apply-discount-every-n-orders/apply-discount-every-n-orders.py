class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.prices = {products[i]:prices[i] for i in range(len(products))}
        self.n = n
        self.discount = discount
        self.cus = 0
        
    def getBill(self, product: List[int], amount: List[int]) -> float:
        total_bill = 0
        
        for i in range(len(product)):
            total_bill += self.prices[product[i]] * amount[i]
        
        self.cus += 1
        if self.cus % self.n == 0:
            return total_bill * (100 - self.discount) / 100
        
        return total_bill