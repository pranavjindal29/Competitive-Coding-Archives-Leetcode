class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        rank = [0] * n
        parent = list(range(n))

        def findRoot(i) -> int:
            if parent[i] != i:
                parent[i] = findRoot(parent[i])
            return parent[i]

        def merge(a, b):
            root_a = findRoot(a)
            root_b = findRoot(b)
            if root_a == root_b:
                return
            rank_a = rank[root_a]
            rank_b = rank[root_b]
            if rank_a > rank_b:
                parent[root_b] = root_a
            elif rank_a < rank_b:
                parent[root_a] = root_b
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

        for a, b in pairs:
            merge(a, b)
        
        root_to_options = defaultdict(list)
        for i in range(n):
            root = findRoot(i)
            root_to_options[root].append(s[i])

        for options in root_to_options.values():
            options.sort(reverse=True)
        
        smallest_string = []
        for i in range(n):
            root = findRoot(parent[i])
            char = root_to_options[root].pop()
            smallest_string.append(char)
        return "".join(smallest_string)