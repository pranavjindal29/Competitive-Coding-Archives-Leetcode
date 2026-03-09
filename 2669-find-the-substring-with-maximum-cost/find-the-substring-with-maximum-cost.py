class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        seen, max_cost = {c : v for c, v in zip(chars, vals)}, 0
        max_cost_substring_ending_at_cur = 0
        for c in s:
            v = seen.get(c, ord(c) - ord('a') + 1)
            max_cost_substring_ending_at_cur = max(max_cost_substring_ending_at_cur + v, v)
            max_cost = max(max_cost, max_cost_substring_ending_at_cur)
        return max_cost      