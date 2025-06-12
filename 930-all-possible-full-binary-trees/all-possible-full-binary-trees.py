class Solution:
    def __init__(self):
        self.dp = []

    def solve(self, n):
        if n % 2 == 0:
            return []

        if self.dp[n]:
            return self.dp[n]

        if n == 1:
            new_node = TreeNode(0)
            return [new_node]

        res = []
        for i in range(1, n, 2):
            left = self.solve(i)
            right = self.solve(n - i - 1)

            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    res.append(root)

        self.dp[n] = res
        return res

    def allPossibleFBT(self, n: int):
        self.dp = [[] for _ in range(n + 1)]
        return self.solve(n)