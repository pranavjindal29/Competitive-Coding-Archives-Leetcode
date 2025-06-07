class Solution:
    def clearStars(self, s: str) -> str:
        h = []
        stacks = [[] for _ in range(26)]

        for i, c in enumerate(s):
            if c == "*":
                while h and not stacks[h[0]]:
                    heapq.heappop(h)
                if h:
                    stacks[h[0]].pop()
                    if not stacks[h[0]]:
                        heapq.heappop(h)
            else:
                x = ord(c) - ord('a')
                if not stacks[x]:
                    heapq.heappush(h, x)
                stacks[x].append(i)

        result = []
        indices = []
        for stack in stacks:
            indices.extend(stack)
    
        indices.sort()
        return ''.join(s[i] for i in indices)