class Solution:
    def putMarbles(self, weights, k):

        n = len(weights)

        # Edge Case: Not enough marbles or invalid k
        if n <= 1 or k <= 1 or k > n:
            return 0

        # Step 1: Compute pair sums (adjacent elements)
        pair_sums = []
        for i in range(n - 1):
            pair_sums.append(weights[i] + weights[i + 1])

        # Step 2: Sort the pair sums
        pair_sums.sort()

        # Step 3: Compute min and max score using (k-1) smallest/largest pair sums
        min_score = sum(pair_sums[:k - 1])
        max_score = sum(pair_sums[-(k - 1):])

        # Step 4: Return the difference
        return max_score - min_score