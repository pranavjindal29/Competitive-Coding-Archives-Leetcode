import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        bestTime = [[float('inf')] * m for _ in range(n)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Priority queue: (time, x, y, nextMove)
        pq = [(0, 0, 0, 0)]

        while pq:
            time, i, j, nextMove = heapq.heappop(pq)
            if time >= bestTime[i][j]:
                continue
            bestTime[i][j] = time

            if i == n - 1 and j == m - 1:
                return time

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    wait = moveTime[x][y]
                    futureMove = 2 if nextMove == 1 else 1
                    nextTime = wait + futureMove if wait > time else time + futureMove

                    if i == 0 and j == 0 and wait <= time:
                        nextTime = wait + futureMove

                    if nextTime < bestTime[x][y]:
                        heapq.heappush(pq, (nextTime, x, y, futureMove))

        return -1  # Should never reach