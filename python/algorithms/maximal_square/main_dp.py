#!/usr/bin/env python3

class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        size = 0
        height = len(matrix)
        width = len(matrix[0])
        for i in range(height):
            for j in range (width):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                else:
                    if i - 1 >= 0 and j - 1 >= 0:
                        tmp = min(matrix[i - 1][j], matrix[i-1][j - 1], matrix[i][j - 1]) + 1
                    else:
                        tmp = 1
                    matrix[i][j] = tmp
                    size = max(size, tmp)
        return size ** 2

sol = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","1"],["1","0"]]
matrix = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
print(sol.maximalSquare(matrix))