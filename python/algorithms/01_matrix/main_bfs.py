#!/usr/bin/env python3

from collections import deque


class Solution:

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        height = len(mat)
        width = len(mat[0])
        to_see = deque()
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    to_see.appendleft((i,j))
                else:
                    mat[i][j] = -1
        while (to_see):
            i, j = to_see.pop()
            for i1, j1 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= i1 < height and 0 <= j1 < width and mat[i1][j1] == -1:
                    mat[i1][j1] = mat[i][j] + 1
                    to_see.appendleft((i1, j1))
        return (mat)

sol = Solution()
mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
mat = [[0,0,0],[0,0,0],[0,0,0]]
mat = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
mat = [[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]
[print(i) for i in mat]
print("update")
[print(i) for i in sol.updateMatrix(mat)]