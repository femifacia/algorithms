#!/usr/bin/env python3

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0 for i in range(n)] for i in range(n)]
        i,j=0,0
        i_start,j_start = 0,0
        val = 1
        size = n ** 2
        while (val <= size):
            i,j =i_start,j_start
            matrix[i][j] = val
            val += 1
            for a,b in [(0, 1),(1,0),(0,-1),(-1,0)]:
                while 0 <= i + a < n and 0 <= j + b < n and matrix[i + a][j + b] == 0:
                    matrix[i + a][b + j] = val
                    i += a
                    j += b
                    val+=1
            i_start+=1
            j_start+=1
        return matrix
    
sol = Solution()
[print(i) for i in sol.generateMatrix(5)]