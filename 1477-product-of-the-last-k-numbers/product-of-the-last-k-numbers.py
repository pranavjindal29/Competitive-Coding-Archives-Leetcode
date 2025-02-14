class ProductOfNumbers:
    def __init__(self):
        self.list = []
        self.prod = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.list = []
            self.prod = 1
        else:
            self.prod *= num
            self.list.append(self.prod)

    def getProduct(self, k: int) -> int:
        if len(self.list) < k:
            return 0
        if len(self.list) == k:
            return self.list[-1]
        return self.list[-1] // self.list[-k - 1]