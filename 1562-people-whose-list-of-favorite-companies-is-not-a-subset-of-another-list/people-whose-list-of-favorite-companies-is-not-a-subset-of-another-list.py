class Solution:
    def peopleIndexes(self, favoriteCompanies: list[list[str]]) -> list[int]:
        fc = sorted(
            ((set(f), i) for i, f in enumerate(favoriteCompanies)),
            key=lambda x: len(x[0])
        )

        valid = set(range(len(fc)))

        for n, (fc_n, i) in enumerate(fc):
            for fc_m, _ in fc[n + 1:]:
                if fc_n < fc_m:
                    valid.remove(i)
                    break

        return sorted(valid)