class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        # this zip and unzip are for sorting indexes, sources and targets by the indexes
        indexes, sources, targets = zip(*sorted(zip(indexes, sources, targets)))
        res = list(S)
        added = 0
        for i, index in enumerate(indexes):
            n = len(sources[i])
            if S[index : index + n] == sources[i]:
                res[index + added  :index + added + n] = list(targets[i])
                added += len(targets[i]) - len(sources[i])
        return "".join(res)