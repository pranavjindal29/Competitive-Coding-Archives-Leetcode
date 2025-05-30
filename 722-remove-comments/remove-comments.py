class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        new_line = []
        result = []

        for line in source:
            i = 0

            while i < len(line):
                if not in_block:

                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        in_block = True
                        i += 2

                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break

                    else:
                        new_line.append(line[i])
                        i += 1
                else:
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        in_block = False
                        i += 2

                    else:
                        i += 1

            if new_line and not in_block:
                result.append("".join(new_line))
                new_line = []

        return result