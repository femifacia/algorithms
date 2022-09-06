#!/usr/bin/env python3

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_pos = []

        for y in range(m):
            for x in range(n):
                if (matrix[y][x] == 0):
                    zero_pos.append((x, y))
        for x, y in zero_pos:
            matrix[y] = [0] * n
            for i in range (m):
                matrix[i][x] = 0
sol = Solution()
arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(arr)
sol.setZeroes(arr)
print(arr)