class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        context = None
        item = None
        stack = []
        sign = 1

        for token in s:
            if token.isdigit():
                if item is None:
                    item = NestedInteger()
                item.setInteger(10*(item.getInteger() or 0) + sign * int(token))
            elif token == '-':
                sign = -1
            elif token == '[':
                stack.append(context)
                context = NestedInteger()
                item = None
            elif token == ']':
                if item is not None:
                    context.add(item)
                item = context
                context = stack.pop()
            elif token == ',':
                context.add(item)
                item = None
                sign = 1
        return item