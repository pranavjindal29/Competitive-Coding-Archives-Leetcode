class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        length = 1
        numbers = set()
        
        for i in range(len(rolls)):
            numbers.add(rolls[i])
            if len(numbers) >= k:
                numbers = set()
                length += 1
            
        
        return length