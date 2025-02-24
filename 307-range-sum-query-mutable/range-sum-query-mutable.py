class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * 2 * self.n
        for i in range(self.n):
            self.tree[i + self.n] = nums[i]
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
        print(self.tree)

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        while index > 1:
            self.tree[index//2] = self.tree[index] + self.tree[index^1]
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            if left & 1:
                # if left odd:
                res += self.tree[left]
                left += 1
            if right & 1 ==0:
                # if right even
                res += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return res        