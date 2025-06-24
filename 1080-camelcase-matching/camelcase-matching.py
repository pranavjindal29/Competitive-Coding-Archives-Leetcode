class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        answer = []

        for x in queries:
            l = r = 0

            while l < len(pattern) and r < len(x):
                if pattern[l] == x[r]:
                    l += 1
                    r += 1
                else:
                    r += 1

            if l == len(pattern) and all(map(str.islower, Counter(x) - Counter(pattern))):
                answer.append(True)

            else:
                answer.append(False)

        return answer