class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.value = 0
        
class MapSum:
    def __init__(self):
        self.t = TrieNode()
        self.m = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.m.get(key,0)
        self.m[key] = val
        node = self.t
        for char in key:
            node = node.children[char]
            node.value += delta
        
    def sum(self, prefix: str) -> int:
        node = self.t
        for char in prefix:
            node = node.children.get(char)
            if not node:
                return 0
        return node.value
            