class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        conflicts = [[] for _ in range(n + 2)]

        for a, b in conflictingPairs:
            if a < b:
                conflicts[b].append(a)
            else:
                conflicts[a].append(b)
        
        max_left = 0
        second_max_left = 0
        gains = [0] * (n + 2)
        valid_subarrays = 0

        for right in range(1, n + 1):
            for left in conflicts[right]:
                if left > max_left:
                    second_max_left = max_left
                    max_left = left
                elif left > second_max_left:
                    second_max_left = left
            valid_subarrays += right - max_left
            gains[max_left] += max_left - second_max_left

        return valid_subarrays + max(gains)