class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent, diff = {}, []

        def find(x):
            if x not in parent: return x
            else: return find(parent[x])

        for s in equations:                 # <-- 1)
            a, b = s[0], s[3]

            if s[1]== "=":                  # <-- 2)
                x, y = find(a), find(b)
                if x!=y:
                    parent[y] = x
            else:    
                diff.append((a,b))          # <-- 3)

        return all(find(a)!=find(b) for a, b in diff)