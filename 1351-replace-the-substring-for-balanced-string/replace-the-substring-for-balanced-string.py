from collections import Counter
from collections import defaultdict

class Solution:
    def balancedString(self, s: str) -> int:
        extra = Counter(s) - Counter({a: len(s)//4 for a in 'QWER'})
        if not extra:
            return 0
        
        ans = len(s)
        indices = defaultdict(list)
        for i, a in enumerate(s):
            indices[a].append(i)
            if any(len(indices[k]) < v for k, v in extra.items()):
                continue
            ans = min(ans, i - min(indices[k][-v] for k, v in extra.items()) + 1)
        return ans