class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        @cache
        def dfs(level: str) -> bool:
            if len(level) == 1:
                return True

            return any(
                dfs(next_level)
                for next_level in product(*(pool[x + y] for x, y in pairwise(level)))
            )

        pool = defaultdict(list)

        for pattern in allowed:
            pool[pattern[:2]].append(pattern[2])

        return dfs(bottom)