from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        users = defaultdict(set)
        for u, t in logs:
            users[u].add(t)
        answer = [0]*k
        for s in users.values():
            u = len(s)
            if u <= k:
                answer[u-1] += 1
        return answer