class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        currentWinner = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if arr[i] > currentWinner:
                currentWinner = arr[i]
                count = 1
            else:
                count += 1
            if count == k:
                return currentWinner
        return currentWinner