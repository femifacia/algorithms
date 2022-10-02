#!/usr/bin/env python3

from collections import deque
import math


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        self.height = len(mat)
        self.width = len(mat[0])
#        print(self.seen)
        for i in range(self.height):
            for j in range(self.width):
                if (mat[i][j] > 0):
                    left = mat[i][j-1] if j - 1 >= 0 else math.inf
                    top = mat[i - 1][j] if i - 1 >= 0 else math.inf
                    mat[i][j] = min(top, left) + 1
        #return mat
        for i in range(self.height - 1, -1, -1):
            for j in range(self.width -1, -1, -1):
                if (mat[i][j] > 0):
                    right = mat[i][j + 1] if j + 1 < self.width else math.inf
                    bottom = mat[i + 1][j] if i + 1 < self.height else math.inf
                    mat[i][j] = min(right + 1, bottom + 1, mat[i][j])
        return (mat)

sol = Solution()
mat = [[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]
mat = [[0,0,0],[0,0,0],[0,0,0]]
mat = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[1,1,1],[1,1,0],[1,1,1]]
[print(i) for i in mat]
print("update")
[print(i) for i in sol.updateMatrix(mat)]