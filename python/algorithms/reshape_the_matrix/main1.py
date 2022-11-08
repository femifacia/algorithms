#!/usr/bin/env python3

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        height = len(mat)
        width = len(mat[0])
        if r * c != height * width:
            return mat
        ans = [[0] * c for i in range(r)]
        a = 0
        b = 0
        for i in range(r):
            for j in range(c):
                ans[i][j] = mat[a][b]
                b+=1
                if b == width:
                    b = 0
                    a += 1
        return ans
sol = Solution()
mat = [[1,2],[3,4]]
r = 1
c = 4
[print(i) for i in sol.matrixReshape(mat, r, c)]