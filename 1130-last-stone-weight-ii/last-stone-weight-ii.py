class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        prev_state = {0}
        for elem in stones:
            state = set()
            for prev in prev_state:
                state.add(elem + prev)
                state.add(abs(prev - elem))
            prev_state = state
        return min(prev_state)