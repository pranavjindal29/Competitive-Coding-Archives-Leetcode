from typing import List


class Solution:
    def getArr(self, mat, i, j) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        nums = []
        len_i = m - i
        len_j = n - j
        for _ in range(min(len_i, len_j)):
            nums.append(mat[i][j])
            i += 1
            j += 1
        return nums

    def setArr(self, mat, i, j, nums):
        m = len(mat)
        n = len(mat[0])
        len_i = m - i
        len_j = n - j
        for p in range(min(len_i, len_j)):
            mat[i][j] = nums[p]
            i += 1
            j += 1

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat)):
            nums = self.getArr(mat, i, 0)
            nums.sort()
            self.setArr(mat, i, 0, nums)

        for j in range(1, len(mat[0])):
            nums = self.getArr(mat, 0, j)
            nums.sort()
            self.setArr(mat, 0, j, nums)
        return mat