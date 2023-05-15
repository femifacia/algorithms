#!/usr/bin/env python3

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        i_start, j_start = 0,0
        count = 0
        height = len(matrix)
        width = len(matrix[0])
        limit = width * height
        arr = []

        while (count < limit):
            i,j = i_start, j_start
            arr.append(matrix[i][j])
            matrix[i][j] = "0"
            count+=1
            for a,b in [(0,1), (1,0), (0,-1), (-1,0)]:
                while 0 <= i + a < height and 0 <= j + b < width and matrix[i+a][j+b] != "0":
                    arr.append(matrix[i+a][j+b])
                    i+=a
                    j+=b
                    matrix[i][j] = "0"
                    count += 1
            i_start +=1
            j_start += 1
        return arr

sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(matrix))