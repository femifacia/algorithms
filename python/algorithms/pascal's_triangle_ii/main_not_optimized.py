#!/usr/bin/env python

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        #ans = [1] * (rowIndex + 1)

        #return ans

        arr = [[1], [1,1]]
        for i in range(2, rowIndex + 1):
            line = [1] * (i + 1)
            for j in range(1, len(line) - 1):
                line[j] = arr[-1][j] + arr[-1][j-1]
            arr.append(line)
        return arr[rowIndex]
