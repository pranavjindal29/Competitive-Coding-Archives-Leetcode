class Solution(object):
    def colorTheGrid(self, m, n):
        MOD = 10**9 + 7
        from itertools import product
        from collections import defaultdict

        # Step 1: Generate all valid column states with no vertical same colors
        def is_valid(state):
            for i in range(1, len(state)):
                if state[i] == state[i - 1]:
                    return False
            return True

        colors = [1, 2, 3]
        all_states = [p for p in product(colors, repeat=m) if is_valid(p)]

        # Step 2: Precompute transitions between compatible states
        transitions = defaultdict(list)
        for a in all_states:
            for b in all_states:
                if all(x != y for x, y in zip(a, b)):
                    transitions[a].append(b)

        # Step 3: Initialize DP for the first column
        dp = defaultdict(int)
        for state in all_states:
            dp[state] = 1

        # Step 4: DP over columns
        for _ in range(1, n):
            new_dp = defaultdict(int)
            for prev_state in dp:
                for next_state in transitions[prev_state]:
                    new_dp[next_state] = (new_dp[next_state] + dp[prev_state]) % MOD
            dp = new_dp

        # Step 5: Sum all final counts
        return sum(dp.values()) % MOD