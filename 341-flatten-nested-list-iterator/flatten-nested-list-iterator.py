class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(nested):
            result = []
            for ni in nested:
                if ni.isInteger():
                    result.append(ni.getInteger())
                else:
                    result.extend(flatten(ni.getList()))
            return result
        
        self.flattened = flatten(nestedList)
        self.index = 0

    def next(self) -> int:
        self.index += 1
        return self.flattened[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.flattened)