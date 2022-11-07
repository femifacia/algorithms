#!/usr/bin/env python3

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res = 0
        i = 0
        j1 = 0
        size =len(mat[0])
        j2 = size - 1
        while (i < size):
            res += mat[i][j1]
            res += mat[i][j2]
            i+=1
            j1 += 1
            j2 -= 1
        return res if size % 2 == 0 else res - mat[size//2][size//2]