class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def find(i):
            if manager[i] > -1:
                informTime[i] += find(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(map(find, range(n)))