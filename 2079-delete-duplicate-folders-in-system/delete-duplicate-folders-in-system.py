class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree = {}
        for path in paths:
            curr = tree
            for name in path:
                curr = curr.setdefault(name, {})

        def encode(node):
            if not node:
                return "()"
            parts = []
            for key, sub in node.items():
                parts.append(key + encode(sub))
            sign = "".join(sorted(parts))
            store[sign].append(node)
            return "(" + sign + ")"

        def remove(nodes):
            for item in nodes:
                item.clear()
                item["#"] = True

        store = defaultdict(list)
        encode(tree)
        for group in store.values():
            if len(group) > 1:
                remove(group)

        def collect(node, path):
            for key, sub in list(node.items()):
                if "#" in sub:
                    continue
                new = path + [key]
                result.append(new)
                collect(sub, new)

        result = []
        collect(tree, [])
        return result