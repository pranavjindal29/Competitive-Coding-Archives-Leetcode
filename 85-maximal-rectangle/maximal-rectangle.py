class Solution:
    def area(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)

        for i in range(n + 1):
            h = 0 if i == n else heights[i]
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        hist = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    hist[j] += 1
                else:
                    hist[j] = 0
            ans = max(ans, self.area(hist))

        return ans