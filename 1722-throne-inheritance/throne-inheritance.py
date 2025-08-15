class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dead = set()
        self.graph = {kingName: []}
        self.root = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph.setdefault(parentName, []).append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        
        def dfs(n):
            """Pre-order traverse the graph."""
            if n not in self.dead: ans.append(n)
            for nn in self.graph.get(n, []): dfs(nn)
        
        ans = []
        dfs(self.root)
        return ans 