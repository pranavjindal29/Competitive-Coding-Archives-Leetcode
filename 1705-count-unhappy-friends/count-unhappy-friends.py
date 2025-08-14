class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n-1):
                rank[i][preferences[i][j]] = j
        
        paired_with = [0] * n
        for x, y in pairs:
            paired_with[x] = y
            paired_with[y] = x

        unhappy_count = 0
        for x in range(n):
            y = paired_with[x]
            for i in range(rank[x][y]):
                u = preferences[x][i]
                v = paired_with[u]
                if rank[u][x] < rank[u][v]:
                    unhappy_count += 1
                    break
        return unhappy_count