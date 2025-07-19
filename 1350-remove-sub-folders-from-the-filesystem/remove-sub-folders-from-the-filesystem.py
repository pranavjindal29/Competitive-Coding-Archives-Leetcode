class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        dirSet = set(folder)
        res = []

        for dir in folder:
            res.append(dir)
            for i in range(len(dir)):
                if dir[i] == '/' and dir[:i] in dirSet:
                    res.pop()
                    break

        return res