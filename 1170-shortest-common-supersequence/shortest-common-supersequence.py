from concurrent.futures import ThreadPoolExecutor

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        with ThreadPoolExecutor() as executor:
            future = executor.submit(self.generateLCS, str1, str2)
            return future.result()

    def generateLCS(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        lcsMatrix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    lcsMatrix[i][j] = lcsMatrix[i - 1][j - 1] + 1
                else:
                    lcsMatrix[i][j] = max(lcsMatrix[i - 1][j], lcsMatrix[i][j - 1])

        row, col = m, n
        result = []

        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                result.append(str1[row - 1])
                row, col = row - 1, col - 1
            elif lcsMatrix[row - 1][col] > lcsMatrix[row][col - 1]:
                result.append(str1[row - 1])
                row -= 1
            else:
                result.append(str2[col - 1])
                col -= 1

        while row > 0:
            result.append(str1[row - 1])
            row -= 1
        while col > 0:
            result.append(str2[col - 1])
            col -= 1

        return "".join(result[::-1])