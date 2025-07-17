class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        
        def dfs(index):
            if index < 0 or index >= len(arr) or index in visited:
                return False
            if arr[index] == 0:
                return True
            visited.add(index)
            forward_jump = dfs(index + arr[index])
            backward_jump = dfs(index - arr[index])
            return forward_jump or backward_jump
        return dfs(start)