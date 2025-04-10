from random import randint
class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.rows = n_rows
        self.cols = n_cols
        self.len_range = n_rows * n_cols
        self.upper_limit = self.len_range - 1
        self.used = set()

    def flip(self):
        val = randint(0, self.upper_limit)
        while val in self.used:
            val += 1
            if val == self.len_range:
                val = 0
        self.used.add(val)
        return list(divmod(val, self.cols))

    def reset(self) -> None:
        self.used = set()