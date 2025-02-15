class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        stack = [(1, [], 0)]

        while stack:
            i, curr, curr_sum = stack.pop()

            if len(curr) == k and curr_sum == n:
                ans.append(curr)
                continue
            
            if len(curr) >= k or curr_sum >= n:
                continue

            for j in range(i, 10):
                stack.append((j + 1, curr + [j], curr_sum + j))

        return ans