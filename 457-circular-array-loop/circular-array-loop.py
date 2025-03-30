class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        n = len(nums)

        # Create adjacency list
        adj = [[] for _ in range(n)]

        for i in range(n):
            a = (i + nums[i] + n) % n  # Calculate next index with wrap-around
            if a != i:  # Ignore self-loops
                adj[i].append(a)

        visited = [False] * n
        inRec = [False] * n

        # Check if all elements in the cycle move in the same direction
        def same_direction(u, v):
            return (nums[u] > 0) == (nums[v] > 0)

        def dfs(u, visited, inRec):
            visited[u] = True
            inRec[u] = True

            for v in adj[u]:
                # Ensure all elements are in the same direction
                if not same_direction(u, v):
                    continue

                if inRec[v]:  # Cycle detected
                    return True

                if not visited[v] and dfs(v, visited, inRec):
                    return True

            inRec[u] = False
            return False

        # Check each node for a valid cycle
        for i in range(n):
            if not visited[i]:
                if dfs(i, visited, inRec):
                    return True

        return False