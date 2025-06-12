class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        span = 1
        last_span = 0
        while self.stack and price >= self.stack[-1][0]:
            value, last_span = self.stack.pop() 
            span += last_span
        self.stack.append((price, span)) 
        return span


