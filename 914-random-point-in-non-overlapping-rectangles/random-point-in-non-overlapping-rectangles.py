class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        for rect in rects:
            self.weights.append((rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1))
        self.total = sum(self.weights)
        for i in range(1, len(self.weights)):
            self.weights[i] += self.weights[i - 1]
        self.weights = [0] + self.weights
        

    def pick(self) -> List[int]:
        index = bisect.bisect_left(self.weights, random.randint(1, self.total))
        rect = self.rects[index - 1]
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]
