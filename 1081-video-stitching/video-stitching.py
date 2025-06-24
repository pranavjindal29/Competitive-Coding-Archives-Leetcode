class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        stack = [[0,0]]
        for c in sorted(clips, key=lambda c: c[0]):
            while len(stack) > 1 and stack[-2][1] >= c[0] and stack[-1][1] < c[1]:
                stack.pop()
            if stack[-1][1] < c[0]: break
            if c[1] >= time: return len(stack)
            stack.append(c)
        return -1